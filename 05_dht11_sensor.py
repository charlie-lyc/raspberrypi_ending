from time import sleep

### Working anyway... But Not Support Raspberrypi4...
### Issue on 'Beaglebone_Black_Driver'
import Adafruit_DHT 
SENSOR = Adafruit_DHT.DHT11

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR, 23)
        if temperature is not None and humidity is not None:
            print('Temperature: {} Celsius'.format(temperature))
            print('Humidity: {} %RH'.format(humidity))            
        else:
            print('Failed to Load Data!')
    sleep(3)
except KeyboardInterrupt:
    pass
