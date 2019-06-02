import logging

import RPi.GPIO as GPIO

from pyhap.accessory import Accessory
from pyhap.const import CATEGORY_SWITCH


class Switch(Accessory):

    category = CATEGORY_SWITCH

    def __init__(self, *args, pin=11, **kwargs):
        super().__init__(*args, **kwargs)

        serv_switch = self.add_preload_service('Switch')
        self.char_on = serv_switch.configure_char(
            'On', setter_callback=self.set_switch)

        self.pin = pin
        self._gpio_setup(pin)
        self._uid = ""

    @classmethod
    def _gpio_setup(_cls, pin):
        if GPIO.getmode() is None:
            GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)

    def __setstate__(self, state):
        self.__dict__.update(state)
        self._gpio_setup(self.pin)

    def set_switch(self, value):
        if value:
            GPIO.output(self.pin, GPIO.HIGH)
        else:
            GPIO.output(self.pin, GPIO.LOW)

    def stop(self):
        super().stop()
        GPIO.cleanup()
        
    @property
    def uid(self):
        return self._uid
    
    @uid.setter
    def uid(self, identify):
        self._uid = identify