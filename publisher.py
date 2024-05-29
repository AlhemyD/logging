#publisher
import paho.mqtt.client as mqtt_client
import logging, sys, random, requests, time, platform, json
from logging.handlers import TimedRotatingFileHandler

broker="broker.emqx.io"

FORMATTER_STRING = "%(asctime)s — %(name)s — %(levelname)s — %(message)s"
FORMATTER = logging.Formatter(FORMATTER_STRING)
LOG_FILE = "my_app.log"

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    logger.addHandler(console_handler)

    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
    file_handler.setFormatter(FORMATTER)
    logger.addHandler(file_handler)

    return logger

logger=get_logger("publisher")

def get_user_id():
    URL="http://localhost:8000/register"
    
    try:
        response=requests.get(URL)
        if (response.status_code==200):
            return json.loads(response.text)["registered_id"]
        else:
            logger.debug(f"{platform.platform()} Status: {response.status_code}")
            logger.error(f"{platform.platform()} Server error: {response.text}")
    except Exception as e:
        logger.error(f"{platform.platform()} - Server error: {e}")
        return ""
        

uid=get_user_id()
if uid:    
    try:
        client = mqtt_client.Client(
            mqtt_client.CallbackAPIVersion.VERSION1, 
            uid
        )
        logger.info(f"{platform.platform()} - UID: {uid} - Connecting to broker {broker}")
        client.connect(broker)
        client.loop_start() 
        n=random.randint(1,10)
        logger.info(f"{platform.platform()} - UID: {uid} - Publishing {n} publications on 'lab/leds/state'")
        for i in range(n):
            state = "on" if i%2 == 0 else "off"
            state = state + "ArtemV"
            client.publish("lab/leds/state", state)
            logger.info(f"{platform.platform()} - UID: {uid} - published a message: {state}")
            time.sleep(2)
        
        logger.info(f"{platform.platform()} - disconnecting user UID: {uid}")
        client.disconnect()
        client.loop_stop()
    except Exception as e:
        logger.error(f"{platform.platform()} - UID: {uid} - Error on creating an mqtt_client: {e}")


else:
    logger.error(f"{platform.platform()} - Error getting user id for publisher")
