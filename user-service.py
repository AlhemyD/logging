from fastapi import FastAPI
import hashlib, datetime, uvicorn, logging, sys
from logging.handlers import TimedRotatingFileHandler
import platform

app = FastAPI()

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

logger = get_logger("User-Service")


@app.get("/register")
async def register():
    logger.info(f"{platform.platform()} - GET /register - Registering new user")
    print(f"{platform.platform()} - GET /register - Registering new user")
    time_str = str(datetime.datetime.now())  
    id=hashlib.md5(time_str.encode()).hexdigest()   
    file = open("users.txt",'r',encoding='utf-8').readlines()
    while any(line.strip() == id for line in file):
        logger.warning(f"{platform.platform()} - GET /register - Generating another id")
        print(f"{platform.platform()} - GET /register - Generating another id")
        time_str = str(datetime.datetime.now())  
        id=hashlib.md5(time_str.encode()).hexdigest() 
    with open("users.txt",'a') as txt_file:
        txt_file.write(f"{id}"+"\n")
    logger.info(f"{platform.platform()} - GET /register - Registered user. ID: {id}")
    print(f"{platform.platform()} - GET /register - Registered user. ID: {id}")
    return {"registered_id":id}
    

if __name__=="__main__":
    logger.info(f"{platform.platform()} - Server works")
    print(f"{platform.platform()} - Server works")
    uvicorn.run(app,host="0.0.0.0", port=8000)
    if KeyboardInterrupt:
        logger.info(f"{platform.platform()} - Server shutting down")
