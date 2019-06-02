import logging

import RPi.GPIO as GPIO

from pyhap.accessory import Accessory
from pyhap.const import CATEGORY_LIGHTBULB


class BrightBulb(Accessory):

    category = CATEGORY_LIGHTBULB

    def __init__(self, *args, pin=11, **kwargs):
        super().__init__(*args, **kwargs)

        serv_light = self.add_preload_service(
            'Lightbulb', chars=['Brightness'])

        self.char_on = serv_light.configure_char(
            'On', setter_callback=self.set_bulb)

        self.char_brightness = serv_light.configure_char(
            'Brightness', setter_callback=self.set_brightness)

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

    def set_bulb(self, value):
        if value:
            GPIO.output(self.pin, GPIO.HIGH)
        else:
            GPIO.output(self.pin, GPIO.LOW)

    def set_brightness(self, value):
        logging.debug("Brightness set: %s", value)
##        print("Brightness: %s", value)

    def stop(self):
        super().stop()
        GPIO.cleanup()

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, identify):
        self._uid = identify