import RPi.GPIO as GPIO
import requests
import os
import schedule
from time import sleep

led_pin = 26 

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT, initial=0)

def check_internet():
    timeout = 10
    try:
        requests.head('SOME WEB SITE', timeout=timeout)
        
    except:
       for i in range(36):
            flash(3)
            sleep(5)
        pass
        os.system('python /home/pi/Documents/Code/ac_alert.py')

def flash(n):
    for i in range (n):
        GPIO.output(led_pin, 1)
        sleep(0.2)
        GPIO.output(led_pin, 0)
        sleep(0.2)

schedule.every(5).seconds.do(flash, 1)
schedule.every(180).seconds.do(check_internet)

try:
    while True:
        schedule.run_pending()
             
except KeyboardInterrupt:
    print('Clean up')
    GPIO.cleanup()
        
finally:
    print('Clean up')
    GPIO.cleanup()
            
