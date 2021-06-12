import subprocess
import time
import gpiozero
import logging
import threading

POWER_SWITCH_GPIO = 3
STATSFILE = '/proc/diskstats'
FIELD = 12
INTERVAL = 0.05
SSD_LED_GPIO = 21
ACTIVE_HIGH = True

led = gpiozero.LED(SSD_LED_GPIO,
                   active_high=ACTIVE_HIGH,
                   )

encoder = gpiozero.RotaryEncoder(21, 20)

switch = gpiozero.Button(POWER_SWITCH_GPIO)

def power_switch():
    if switch.wait_for_inactive():
        subprocess.run("/usr/bin/lxde-pi-shutdown-helper")
