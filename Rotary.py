import Queue
import threading
from time import sleep

# This seems to work with the common pin on
# the optical encoder at 3.3v and a 22k resistor
# on each switch pin to ground.

class RotaryEncoder(threading.Thread):
    """Given a queue on startup it spits out
events to the queue with either "cw" or "ccw"
"""

    DoRun = True

    def __init__(self, queue, encoder_name, pins, gpio):
        """ Expects a queue to send events to
and an array of the two input pins
"""
        threading.Thread.__init__(self)
        self.queue = queue
        self.pin_a = pins[0]
        self.pin_b = pins[1]
        self.encoder_name = encoder_name
        self.gpio = gpio
        for pin in pins:
            #print "Setting up pin: %s" % pin
            self.gpio.setup(pin, self.gpio.IN, self.gpio.PUD_OFF)
            self.gpio.add_event_detect(pin, self.gpio.RISING)
            
    def stop(self):
        self.DoRun = False

    def run(self):
        while self.DoRun:
            if self.gpio.event_detected(self.pin_a):
                # Ignore false triggers
                if self.gpio.input(self.pin_a) != 1:
                    continue
                level_b = 0
                # De-bounce
                debounce_limit = 10 
                for count in range(0,debounce_limit):
                    level_b += self.gpio.input(self.pin_b)
                    #sleep(0.000001)
                    #print(str(level_b))
                if level_b > 5:
                    dir = "cw"
                else:
                    dir = "ccw"
                self.queue.put(dir)
                sleep(0.005)            
