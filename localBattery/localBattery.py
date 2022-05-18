import psutil
import playsound
from playsound import playsound

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if(percent == 95):
    playsound('95.mp3')
elif(percent == 30):
    playsound('30.mp3')
