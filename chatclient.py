chatting = False
from datetime import datetime
import json
from uuid import getnode as get_mac
mac = str(get_mac())
with open("users.json","r") as check:
    auth = json.load(check)
if mac in auth.keys():
    user = auth[mac]
else:
    user = input("Username: ")
    with open("users.json","r") as check:
        auth = json.load(check)
        if user in auth:
            print("The user name "+str(user)+" is all ready taken!\n")
        else:
            auth[mac] = user
            with open('users.json', 'w') as f:
                json.dump(auth, f)
while not chatting:
    msg = input(str(user)+"> ")
    if msg == "":
        print(open("chatlog.txt", "r").read())
    else:
        msg = str(datetime.now()) + ": "+ str(user)+"> "+msg+ "\n"
        open("chatlog.txt", "a").write(msg)
        print(open("chatlog.txt", "r").read())
