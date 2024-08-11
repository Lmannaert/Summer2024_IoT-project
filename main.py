from lib.functions import *
from lib.wifiConnection import *
import time


DELAY = 60  # Delay in seconds between posts

lib.wifiConnection.connect()
while True:
    temp, hum = datacollection()
    lamp, darkness = lightRead(ldr)
    switch = tiltSwitch()
    sendData(lib.keys.DEVICE_LABEL, lib.keys.VARIABLE_LABEL1, temp)
    sendData(lib.keys.DEVICE_LABEL, lib.keys.VARIABLE_LABEL2, hum)
    sendData(lib.keys.DEVICE_LABEL, lib.keys.VARIABLE_LABEL3, darkness)
    sendData(lib.keys.DEVICE_LABEL, lib.keys.VARIABLE_LABEL4, lamp)
    sendData(lib.keys.DEVICE_LABEL, lib.keys.VARIABLE_LABEL5, switch)
    if switch == 0:
        redLed()
        break
    time.sleep(DELAY)



# WiFi disconnection
#wifiConnection.disconnect()