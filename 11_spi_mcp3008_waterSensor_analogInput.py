from time import sleep
import spidev


CHANNEL = 0
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 100000

def read_analog(channel):
    if channel > 7 or channel < 0:
        return -1
    r = spi.xfer2([1, 8 + channel << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

try:
    while True:
        value = read_analog(CHANNEL) # 1 ~ 1023
        if value != -1:
            print('Water Sensor: {}'.format(value))
        else:
            print('Failed to read data!')
        sleep(0.5)
except KeyboardInterrupt:
    print('Stopped by Keyboard Interrupt')