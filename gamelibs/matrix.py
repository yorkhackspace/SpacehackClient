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
            self.port.write('0\n')

    def loadAnimations(self):
        pass

    def animate(self, name):
        pass

    def test(self):
        if self.port:
            self.port.write('500 08 55aa55aa55aa55aa\n')
            self.port.write('500 07 aa55aa55aa55aa55\n')
            self.port.write('500 06 55aa55aa55aa55aa\n')
            self.port.write('500 05 aa55aa55aa55aa55\n')
            self.port.write('500 04 55aa55aa55aa55aa\n')
            self.port.write('500 03 aa55aa55aa55aa55\n')
            self.port.write('500 02 55aa55aa55aa55aa\n')
            self.port.write('500 01 aa55aa55aa55aa55\n')
            self.port.write('500 00 0000000000000000\n')
            self.port.write('0\n')
