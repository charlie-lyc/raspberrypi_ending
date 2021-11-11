from time import sleep

## Install package
# $ sudo pip3 install Adafruit_Python_DHT

# import Adafruit_DHT


# SENSOR = 24 # BCM mode
# try:
#     while True:
#         humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, SENSOR)
#         if temperature is not None and humidity is not None:
#             print('Temperature: {} Celsius'.format(temperature))
#             print('Humidity: {} %RH'.format(humidity))            
#         else:
#             print('Failed to Load Data!')
#         sleep(3)
# except KeyboardInterrupt:
#     pass


#################################################
### Adafruit_Python_DHT LIBRARY IS DEPRECATED ###
#################################################
## Not support Raspberrypi 4!


## So, install other packgage
# $ sudo pip3 install adafruit-circuitpython-dht
# $ sudo apt install gpiod libgpiod-dev

import adafruit_dht
import board        # BCM mode


dht_device = adafruit_dht.DHT11(board.D24) # board.D24: GPIO-24

### Working anyway...
### But, often happened RuntimeError...

while True:
    try:
        temperature = dht_device.temperature
        humidity = dht_device.humidity
        if temperature is not None and humidity is not None:
            print('Temperature: {} Celsius'.format(temperature))
            print('Humidity: {} %RH'.format(humidity))            
        else:
            print('Failed to Load Data!')
        sleep(3)
    except RuntimeError as error:
        print(error.args[0])
        sleep(3)
        continue
    except Exception as error:
        dht_device.exit()
        raise error