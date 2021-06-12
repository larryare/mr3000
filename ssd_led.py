import subprocess
import time
import gpiozero
import logging


STATSFILE = '/proc/diskstats'
FIELD = 12
INTERVAL = 0.05
GPIO = 21
ACTIVE_HIGH = True

led = gpiozero.LED(GPIO,
                   active_high=ACTIVE_HIGH,
                   )


while True:
    try:
        with open(STATSFILE,mode='r') as s:
            stats = s.read()
            disc_active = False
        for l in stats.split('\n'):
            try:
                if int(l.split()[FIELD - 1]):
                    disc_active = True
                    break
            except IndexError:
                pass
        led.value = disc_active
        time.sleep(INTERVAL)
    except Exception:
        if args.debug:
            raise
        else:
            logging.exception('')
