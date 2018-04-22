# Basic matrix test util

config = {
    'local': { 'buses': { 'matrix': { 'port': '/dev/ttyUSB0' } } }
}

from gamelibs import matrix
import sys
import time

ledMatrix = matrix.Matrix(config)
ledMatrix.clear()

if len(sys.argv) > 1:
    for animation in sys.argv[1:]:
        ledMatrix.animate(animation)
        time.sleep(3)
else:
    ledMatrix.test()
