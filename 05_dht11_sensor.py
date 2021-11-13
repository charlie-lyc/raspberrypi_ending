from time import sleep

## Install package
# $ sudo pip3 install Adafruit_Python_DHT
## Add some codes like below for supporting Raspberrypi4 hardware(BCM2711) 
# /usr/local/lib/python3.7/dist-packages/Adafruit_DHT/platform_detect.py
# ...
# elif match.group(1) == 'BCM2711':
#     return 3
# ...
## Run
# $ python3 05_dht11_sensor  

import Adafruit_DHT


SENSOR = 24 # BCM mode
try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, SENSOR)
        if temperature is not None and humidity is not None:
            print('Temperature: {} Celsius'.format(temperature))
            print('Humidity: {} %RH'.format(humidity))            
        else:
            print('Failed to Load Data!')
        sleep(3)
except KeyboardInterrupt:
    print('Stopped by Keyboard Interrupt')

#################################################
### Adafruit_Python_DHT LIBRARY IS DEPRECATED ###
#################################################
#################################################
## Use other packgages
# $ sudo pip3 install adafruit-circuitpython-dht
# $ sudo apt install gpiod libgpiod-dev
## Working anyway but often happened RuntimeError!
#################################################

# import adafruit_dht
# import board        # BCM mode


# dht_device = adafruit_dht.DHT11(board.D24) # board.D24: GPIO-24
# while True:
#     try:
#         temperature = dht_device.temperature
#         humidity = dht_device.humidity
#         if temperature is not None and humidity is not None:
#             print('Temperature: {} Celsius'.format(temperature))
#             print('Humidity: {} %RH'.format(humidity))            
#         else:
#             print('Failed to Load Data!')
#         sleep(3)
#     except RuntimeError as error:
#         print(error.args[0])
#         sleep(3)
#         continue
#     except Exception as error:
#         dht_device.exit()
#         raise error