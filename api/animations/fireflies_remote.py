from bibliopixel import colors
import random
import time
import os
import sys

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
from base_remote_strip import BaseRemoteStrip

class FireFliesRemote(BaseRemoteStrip):
    def __init__(self, layout, **args):
        super(FireFliesRemote, self).__init__(layout, 0, -1)
        self._count = 7
        self._width = 3
        self._delay_time = 0
        self._slow = 'false'

    def pre_run(self):
        self._step = 0

    def step(self, amt=1):
        amt = 1
        if self._step > self.layout.numLEDs:
            self._step = 0

        self.layout.all_off()

        hue = int(self._color_control)
        bright = int(self._brightness_control)

        for count in range(int(self._count)):
            pixel = random.randint(0, self.layout.numLEDs - 1)

            for width in range(int(self._width)):
                if pixel + count < self.layout.numLEDs:
                    c = colors.hue2rgb(hue % 255)
                    c = colors.color_scale(c, random.randint(bright-10, bright+10))
                    self.layout.set(pixel + width, c)

        self._step += amt
        if self._slow == 'true':
            time.sleep(0.5)