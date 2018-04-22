#spacehack game client LED matrix utility library

import os
import serial
import string

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
        self.animations = {}
        tr = string.maketrans('.x','01')
        for filename in os.listdir('animations'):
            if filename.endswith(".txt"):
                name = filename.rsplit('.',1)[0]
                print("Loading animation " + name)
                animation = ''
                with open('animations/' + filename, 'r') as f:
                    frame = ''
                    for line in f:
                        line = line.strip()
                        if line:
                            if line[0] in ['.','x']:
                                lineval = int(line.translate(tr), 2)
                                if lineval < 0:
                                    lineval = 0
                                    print "Bad line in animation %s: %s" % (filename, line)
                                if lineval > 255:
                                    lineval = 255
                                frame += '%02x' % lineval
                            else:
                                frame += line + ' '
                        else:
                            animation += frame + '\n'
                            frame = ''
                    if frame:
                        animation += frame + '\n'
                self.animations[name] = animation

    def animate(self, name):
        if self.port and name in self.animations:
            self.port.write(self.animations[name])
            self.port.write('0\n')

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
