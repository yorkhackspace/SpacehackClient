#spacehack game client LED matrix utility library

import serial

class Matrix(object):
    def __init__(self, config):
        buses = config['local']['buses']
        if 'matrix' in buses:
            self.port = serial.Serial(buses['matrix']['port'])
        else:
            self.port = False
        self.loadAnimations()

    def clear(self):
        if self.port:
            self.port.write('1000 0 00 00 00 00 00 00 00 00')

    def loadAnimations(self):
        pass

    def animate(self, name):
        pass
