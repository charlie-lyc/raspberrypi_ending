from time import sleep

## Install package
# $ cd ~
# $ sudo apt install python3-dev
# $ git clone https://github.com/doceme/py-spidev
# $ cd py-spidev
# $ sudo python3 setup.py install

import spidev


CHANNEL = 0
spi = spidev.SpiDev()     # Create object
spi.open(0, 0)            # Start SPI communication
spi.max_speed_hz = 100000 # Set communication speed

def read_analog(channel):
    if channel > 7 or channel < 0:
        return -1
    #######################################
    r = spi.xfer2([1, 8 + channel << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    #######################################
    return data

try:
    while True:
        value = read_analog(CHANNEL) # 0 ~ 1023
        if value != -1:
            print('Variable Resistance: {}'.format(value))
        else:
            print('Failed to read data!')
        sleep(0.5)
except KeyboardInterrupt:
    print('Stopped by Keyboard Interrupt')