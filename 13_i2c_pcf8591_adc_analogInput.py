from time import sleep

## Install package
# $ sudo apt install python3-smbus

import smbus


address = 0x48 # Address of ADC/DAC on I2C bus
AIN0 = 0x40    # Photo resistor(LDR sensor)
AIN1 = 0x41    # Thermo resistor
AIN2 = 0x42    
AIN3 = 0x43    # Variable resistor
bus = smbus.SMBus(1) # Initialize I2C bus as Raspberrypi(1)

try:
    while True:
        ## Write input analog value 
        bus.write_byte(address, AIN0)
        # bus.write_byte(address, AIN1)
        # bus.write_byte(address, AIN3)

        ## Read analog value
        value = bus.read_byte(address)
        voltage = value * 3.3 / 255
        print('Aanalog Digital Converter - Value | Voltage : {:>5} | {:>5.3f}'.format(value, voltage))
        sleep(0.5)
except KeyboardInterrupt:
    print('Stopped by Keyboard Interrupt')