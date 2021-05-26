import psutil
import pyttsx3 as r
from time import sleep
import random
import datetime

l_r=["hello sir","hai sir","sir"]
engine = r.init()
engine.setProperty('rate',130)
def speak(text):
    engine.say(text)
    engine.runAndWait()
i=0
s=1
while True:
    l=str(datetime.datetime.now()).split()
    l=l[1].split(":")
    battery=str(psutil.sensors_battery())
    battery=battery[9:].split(",")
    percentage=battery[0].split("=")
    percentage=percentage[1]
    status=battery[2].split("=")
    status=status[1]
    try:
        status=status[:status.index(")")]
    except:
        pass
    if i==0:
        min_=int(l[1])
        i+=1
    c=random.choice(l_r)
    if s==1:
        if (int(percentage)>10 and int(percentage)<20) and status=="False":
            speak(c+", there is only "+percentage+" percent of charge available in your system . please charge the battery")
            s+=1
        elif int(percentage)<=10 and status=='False':
            speak(c+", The battery is about to die, the system has only"+percentage+"percent of charge . please charge the battery")
            s+=1
    if (int(l[1])%5==0 and min_!=l[1]):
        if (int(percentage)>10 and int(percentage)<20) and status=="False":
            speak(c+", there is only "+percentage+" percent of charge available in your system . please charge the battery")
        elif int(percentage)<=10 and status=='False':
            speak(c+", The battery is about to die, the system has only"+percentage+"percent of charge . please charge the battery")
        elif int(percentage)==100 and status=='True':
            speak(c+", the battery is fully charged . please switch off the charger")
        elif int(percentage)==99 and status=='True':
            speak(c+", the battery is charged to "+str(percentage)+"percent . please switch off the charger")
        else:
            pass
        i+=1
        min_=l[1]
