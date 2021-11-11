from time import sleep
import spidev


SW = 0
VRX = 1
VRY = 2
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
        x_position = read_analog(VRX) # Left ~ Right: 0 ~ 1023
        y_position = read_analog(VRY) # Up ~ Down: 0 ~ 1023
        switch = read_analog(SW)      # Not pushed, Pushed: 1023, 0
        if x_position != -1 and y_position != -1 and switch != -1:
            print('X, Y, Switch: {}, {}, {}'.format(x_position, y_position, switch))
        else:
            print('Failed to read data!')
        sleep(0.5)
except KeyboardInterrupt:
    print('Stopped by Keyboard Interrupt')