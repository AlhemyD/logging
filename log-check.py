logs=open("my_app.log",'r', encoding="utf-8").readlines()

apps=["User-Service",'subscriber','publisher']

key_words={
    "User-Service":[
        "Registering",
        "Registered"
    ],
    "subscriber":[
        "Connecting to broker",
        "Subcribing on",
        "recieved"
    ],
    "publisher":[
        "Connecting to broker",
        "Publishing",
        "published a message"
    ]
}
flag=True
for app in apps:
    print(f"Checking {app}")
    for i, line in enumerate(logs):
        if any(j in line for j in apps):
            if app==apps[0] and app in line:            
                if key_words[app][0] in line:
                    try:
                        if i+1 < len(logs) and (not(key_words[app][1] in logs[i+1])):
                            print(f"{app} logs are not correct")
                            flag=False
                            break
                    except Exception as e:
                        print(f"Error: {e}")
                elif key_words[app][1] in line:
                    try:
                        if i-1 >=0 and (not(key_words[app][0] in logs[i-1])):
                            print(f"{app} logs are not correct")
                            flag=False
                            break
                    except Exception as e:
                        print(f"Error: {e}")
                        
            elif app==apps[1] and app in line:
                if key_words[app][0] in line:
                    try:
                        if i+1 < len(logs) and (not(key_words[app][1] in logs[i+1])):
                            print(f"{app} logs are not correct")
                            flag=False
                            break                            
                    except Exception as e:
                        print(f"Error: {e}")
                        
                elif key_words[app][2] in line:
                    try:
                        if i-1 >=0 and (not(key_words["publisher"][2] in logs[i-1])):
                            print(f"{app} logs are not correct")
                            flag=False
                            break
                    except Exception as e:
                        print(f"Error: {e}")
            elif app==apps[2] and app in line:
                if key_words[app][0] in line:
                    try:
                        if i+1 < len(logs) and (not(key_words[app][1] in logs[i+1])):
                            print(f"{app} logs are not correct")
                            flag=False
                            
                            break
                    except Exception as e:
                        print(f"Error: {e}")
                if key_words[app][1] in line:
                    try:
                        if i-1 >=0 and (not(key_words[app][0] in logs[i-1])):
                            print(f"{app} logs are not correct")
                            flag=False
                            
                            break
                        if i+1 < len(logs) and (not(key_words[app][2] in logs[i+1])):
                            print(f"{app} logs are not correct")
                            
                            flag=False
                            break
                    except Exception as e:
                        print(f"Error: {e}")
                
        else:
            print("All logs are incorrect")
            print(line)
            flag=False
            break
if flag:
    print("Logs are correct")
