import logging
import signal

from pyhap.accessory import Bridge
from pyhap.accessory_driver import AccessoryDriver

from homeAutomation.accessories.lightBulb import LightBulb
from homeAutomation.accessories.brightBulb import BrightBulb
from homeAutomation.accessories.switch import Switch
from homeAutomation.accessories.fan import Fan
from homeAutomation.accessories.outlet import Outlet

logging.basicConfig(level=logging.INFO, format="[%(module)s] %(message)s")

def get_bridge(driver):
    bridge = Bridge(driver, 'Bridge')

    Bright1 = BrightBulb(driver, 'Table Lamp')
    Outlet1 = Outlet(driver, 'Table Switch')
    Switch1 = Switch(driver, 'Laptop Charger') 

    Bright1.uid = "BedroomTable Lamp"
    Outlet1.uid = "BedroomTable LaptopCharger"
    Switch1.uid = "BedroomTable Switch"

    bridge.add_accessory(Bright1)
    bridge.add_accessory(Outlet1)
    bridge.add_accessory(Switch1)
    return (bridge)


def run():
        driver = AccessoryDriver(port=51826, persist_file='busy_home.state')
        driver.add_accessory(accessory=get_bridge(driver))
        signal.signal(signal.SIGTERM, driver.signal_handler)
        driver.start()
