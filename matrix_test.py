# Basic matrix test util

config = {
    'local': { 'buses': { 'matrix': { 'port': '/dev/ttyUSB0', 'baud': 9600 } } }
}

from gamelibs import matrix
import sys
import time

ledMatrix = matrix.Matrix(config)
ledMatrix.clear()

if len(sys.argv) > 1:
    ledMatrix.animate(sys.argv[1])
else:
    ledMatrix.test()
