import logging
import paho.mqtt.client as mqtt

from pyhap.accessory import Accessory
from pyhap.const import CATEGORY_FAN

class Fan(Accessory):

    category = CATEGORY_FAN

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        serv_fan = self.add_preload_service(
            'Fan', chars=['RotationSpeed'])

        self.char_on = serv_fan.configure_char(
            'On', setter_callback=self.set_fan)

        self.char_brightness = serv_fan.configure_char(
            'RotationSpeed', setter_callback=self.set_speed)

        self._uid = ""
        self.mqtt_username = "atharv"
        self.mqtt_password = "athu1996"
        self.mqtt_topic = "test"
        self.mqtt_broker_ip = "192.168.1.6"
        
        self.client = mqtt.Client()
        self.client.username_pw_set(self.mqtt_username, self.mqtt_password)
        self.client.on_connect = self.on_connect
        self.client.connect(self.mqtt_broker_ip, 1883)
    
    def on_connect(client, userdata, flag, rc):
        client.subscribe(mqtt_topic)

    def set_fan(self, value):
        data = self._uid + "/" + str(value)
        self.client.publish(self.mqtt_topic, payload=data, retain=False)

    def set_speed(self, value):
        data = self._uid + "!" + str(value)
        self.client.publish(self.mqtt_topic, payload=data, retain=False)

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, identify):
        self._uid = identify
