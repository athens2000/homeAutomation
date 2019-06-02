import logging
import signal

from pyhap.accessory import Bridge
from pyhap.accessory_driver import AccessoryDriver

from homeAutomation.accessories.lightBulb import LightBulb
from homeAutomation.accessories.brightBulb import BrightBulb
from homeAutomation.accessories.switch import Switch
from homeAutomation.accessories.fan import Fan

logging.basicConfig(level=logging.INFO, format="[%(module)s] %(message)s")

def get_bridge(driver):
    bridge = Bridge(driver, 'Bridge')

    Light1 = LightBulb(driver, 'LightBulb', pin=10)
    Bright1 = BrightBulb(driver, 'TableLamp', pin=12)
    Switch1 = Switch(driver, 'TableSwitch', pin=13)
    Fan1 = Fan(driver, 'RoomFan')


    Light1.uid = "Bedroom Light"
    Bright1.uid = "Bedroom Table Lamp"
    Switch1.uid = "Bedroom Laptop Charger"
    Fan1.uid = "Bedroom Fan"

    bridge.add_accessory(Light1)
    bridge.add_accessory(Bright1)
    bridge.add_accessory(Switch1)
    bridge.add_accessory(Fan1)
    return (bridge)


def run():
        driver = AccessoryDriver(port=51826, persist_file='busy_home.state')
        driver.add_accessory(accessory=get_bridge(driver))
        signal.signal(signal.SIGTERM, driver.signal_handler)
        driver.start()import logging
import signal

from pyhap.accessory import Bridge
from pyhap.accessory_driver import AccessoryDriver

from homeAutomation.accessories.lightBulb import LightBulb
from homeAutomation.accessories.brightBulb import BrightBulb
from homeAutomation.accessories.switch import Switch
from homeAutomation.accessories.fan import Fan

logging.basicConfig(level=logging.INFO, format="[%(module)s] %(message)s")

def get_bridge(driver):
    bridge = Bridge(driver, 'Bridge')

    Light1 = LightBulb(driver, 'LightBulb', pin=10)
    Bright1 = BrightBulb(driver, 'TableLamp', pin=12)
    Switch1 = Switch(driver, 'TableSwitch', pin=13)
    Fan1 = Fan(driver, 'RoomFan')


    Light1.uid = "Bedroom Light"
    Bright1.uid = "Bedroom Table Lamp"
    Switch1.uid = "Bedroom Laptop Charger"
    Fan1.uid = "Bedroom Fan"

    bridge.add_accessory(Light1)
    bridge.add_accessory(Bright1)
    bridge.add_accessory(Switch1)
    bridge.add_accessory(Fan1)
    return (bridge)


def run():
        driver = AccessoryDriver(port=51826, persist_file='busy_home.state')
        driver.add_accessory(accessory=get_bridge(driver))
        signal.signal(signal.SIGTERM, driver.signal_handler)
        driver.start()