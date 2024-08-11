import lib.wifiConnection

try:
    ip = lib.wifiConnection.connect()
except KeyboardInterrupt:
    print("Keyboard interrupt")




