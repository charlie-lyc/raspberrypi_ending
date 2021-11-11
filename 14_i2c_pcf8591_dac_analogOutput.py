from time import sleep
import smbus


address = 0x48
ANALOG_OUT = 0x40
bus = smbus.SMBus(1)

try:
    while True: # Built-in LED on and brighter softly, then off
        for value in range(256):
            bus.write_byte_data(address, ANALOG_OUT, value)
            voltage = value * 3.3 / 255
            print('Digital Analog Converter - Value | Voltage : {:>5} | {:>5.3f}'.format(value, voltage))
            sleep(0.01)
except KeyboardInterrupt:
    print('Stopped by Keyboard Interrupt')