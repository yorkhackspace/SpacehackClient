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
    wait=False
    for animation in sys.argv[1:]:
        if wait:
            time.sleep(5)
	print("Testing '%s'" % animation)
        ledMatrix.animate(animation)
        wait=True
else:
    ledMatrix.test()
