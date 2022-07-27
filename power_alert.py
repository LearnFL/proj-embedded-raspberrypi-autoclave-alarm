'''THIS SOFTWARE WAS BUILT BY DENNIS ROTNOV
Feel free to reuse it and change it, but keep authorship attribution please'''

from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import os
from time import sleep
from dotenv import load_dotenv
import RPi.GPIO as GPIO
from datetime import datetime
import requests
import schedule

load_dotenv()

client = Client( os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN') )

class PhoneBook():
    def __init__(self):
        self.name_list = []
        self.phones = {
            'NAME_1': '+1xxxxxxxxxx',   # Enter a name and a phone numeber 
            'NAME_2': '+1xxxxxxxxxx',   # Enter a name and a phone numeber 
            'NAME_3': '+1xxxxxxxxxx'    # Enter a name and a phone numeber 
        }

    def get_numbers(self):
        return list(self.phones.values())
    
    def get_name(self, number):
        for name, phone in self.phones.items():
            if phone == number:
                return(str(name))

    def __repr__(self):
        return f"Object: {self.__class__.__name__!r}, SMS list: {self.phones!r}"


phonebook = PhoneBook()

# LED serves as an indicator that the system is connected to internet
def flash(n):
    for i in range (n):
        GPIO.output(led_pin, 1)
        sleep(0.2)
        GPIO.output(led_pin, 0)
        sleep(0.2)
        

def alert(message):
    try:
        for number in phonebook.get_numbers():
            client.messages.create(to=number,
            from_= os.getenv('FROM'),
            body=message)
            print(f'Sent to {phonebook.get_name(number)}: {message}')
               
    except:
        pass
        # Restarts the code 
        os.system('python /home/pi/Documents/Code/ac_alert.py')
    
def send_power_alert():
    try:
        alert("POWER OUTAGE ALERT")
        sleep(60*10) # to limit number of alerts
    except:
        flash(3)
        pass
        # restart code
        os.system('python /home/pi/Documents/Code/ac_alert.py')
        
    

outage_alarm_pin = 24
led_pin = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(outage_alarm_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT, initial=0)
outage = GPIO.input(outage_alarm_pin)

schedule.every(5).seconds.do(flash, 1)

try:
    while True:
        
        schedule.run_pending()
      
        if GPIO.input(outage_alarm_pin) == 0:
            send_power_alert()
            while GPIO.input(outage_alarm_pin) == 0:
                sleep(0.01)
               
except KeyboardInterrupt:
    print('Clean up')
    GPIO.cleanup()
        
finally:
    print('Clean up')
    GPIO.cleanup()
            
        

   

