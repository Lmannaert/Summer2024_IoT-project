import dht
import time
import network
import machine
import lib.keys
import lib.wifiConnection
import json



tempSensor = dht.DHT11(machine.Pin(22))     # DHT11 Constructor
ldr = machine.ADC(machine.Pin(27))
led = machine.Pin(16, machine.Pin.OUT)
tiltPin = machine.Pin(26, machine.Pin.IN)
offLed = machine.Pin(15, machine.Pin.OUT)


# Builds the json to send the request
def build_json(variable, value):
    try:
        data = {variable: {"value": value}}
        return data
    except:
        return None

def datacollection():
    try:
        tempSensor.measure()
        temperature = tempSensor.temperature()
        humidity = tempSensor.humidity()
        return temperature, humidity
    except Exception as error:
        print("Exception occured", error)



def tiltSwitch():
    if tiltPin.value() == 1:
        print("Switch ON...")
        switch = 100
    else:
        print("Switch OFF...")
        switch = 0
    return switch


def lightRead(ldr):
    light = ldr.read_u16()
    print("Sensor value: ", light)
    darkness = round(light / 65535 * 100, 2)
    if darkness >= 70:
        print("Darkness is {}%, LED turned on".format(darkness))
        lamp = 1 
    else:
        print("It is enough light, no need to turn the LED on")
        lamp = 0
    ledLight(lamp, led)
    return lamp, darkness

def ledLight(lamp, led):
    if lamp == 1:
        led.on()
    elif lamp == 0:
        led.off()

def redLed():
    n = 0
    while n < 10:
        offLed.on()
        time.sleep(0.3)
        offLed.off()
        time.sleep(0.5)
        n += 1   



# Sending data to Ubidots Restful Webserice
def sendData(device, variable, value):
    try:
        url = f"https://industrial.api.ubidots.com/api/v1.6/devices/{device}"
        headers = {"X-Auth-Token": lib.keys.TOKEN, "Content-Type": "application/json"}
        data = build_json(variable, value)

        if data is not None:
            print(data)
            req = requests.post(url=url, headers=headers, json=data)
            return req.json()
        else:
            pass
    except:
        pass


# WiFi connection
#mqtt_client = connect_mqtt()

# Your device send a random value between 0 and 100 every five second to
# Ubidots
