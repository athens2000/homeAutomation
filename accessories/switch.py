import logging
import paho.mqtt.client as mqtt

from pyhap.accessory import Accessory
from pyhap.const import CATEGORY_SWITCH


class Switch(Accessory):

    category = CATEGORY_SWITCH

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        serv_switch = self.add_preload_service('Switch')
        self.char_on = serv_switch.configure_char(
            'On', setter_callback=self.set_switch)

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

    def set_switch(self, value):
    data = self._uid + "/" + str(value)
    self.client.publish(self.mqtt_topic, payload=data, retain=False)
        
    @property
    def uid(self):
        return self._uid
    
    @uid.setter
    def uid(self, identify):
        self._uid = identify
