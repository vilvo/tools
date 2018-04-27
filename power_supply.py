#!/usr/bin/python
# power supply control for generic automation

import serial, getopt, sys

class tenma():
    ''' Implements good parts of remote control protocol for an affordable
        Tenma power supply - tested with Tenma 72-2535 over USB serial
        remote control protocol spec: https://goo.gl/YRNlPu '''
    def __init__(self):
        self.s = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)
    def off(self):
        self.s.write('OUT0')
    def on(self):
        self.s.write('OUT1')
    def setvoltage(self, voltage):
        cmd = "VSET1:%s" % (voltage)
        for x in cmd:
            self.s.write(x)

if __name__ == '__main__':
    power_supply = tenma()
    usage = 'usage: %s -u [0-30] -p [ON|OFF]' % sys.argv[0]

    try:
        opts, args = getopt.getopt(sys.argv[1:],"hu:p:", ["help", "voltage=", "power="])
    except getopt.GetoptError:
        print usage
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print usage
            sys.exit()
        elif opt == '-u':
            try:
                voltage = float(arg)
            except:
                print usage
            if 0.0 <= voltage <= 30.0:
                power_supply.setvoltage(str(voltage))
            else:
                print usage
        elif opt == '-p':
            if arg == 'ON':
                power_supply.on()
            if arg == 'OFF':
                power_supply.off()
            else:
                print usage
