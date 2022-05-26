from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import os
from time import sleep
from dotenv import load_dotenv
import RPi.GPIO as GPIO
from datetime import datetime
import requests
import schedule
#import pigpio

load_dotenv()

client = Client( os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN') )

class PhoneBook():
    def __init__(self):
        self.name_list = []
        self.phones = {
            'Dennis': '+12166739812',
            #'Tom': '+14403449475',
            #'Joe': '+14404943841',
            #'Fred': '+12162721009',
            'James': '+14406690701',
            'Sarah': '+14404173812'
            #'Matt': '+14404138200'
        }

    def get_numbers(self):
        return list(self.phones.values())
    
    def get_name(self, number):
        for name, phone in self.phones.items():
            if phone == number:
                return(str(name))

    def __repr__(self):
        return f"Object: {self.__class__.__name__!r}, SMS list: {self.phones!r}"

class TimeCheck:
    def __init__(self):
        self.start_hour = None
        self.end_hour = None
        self.now = None
        self.today = None
        
    def check_hours(self, start, end):
        condition = False
        
        if self.start_hour is None:
            self.start_hour = start
            
        if self.end_hour is None:
            self.end_hour = end
                
        if self.now is None:
            
            self.now = datetime.now().time()
            
        if (self.now.hour >= self.start_hour) and (self.now.hour <= self.end_hour):
            condition = True
            
        else:
            condition = False
            
        return condition
    
    
    def check_days(self):
        
        condition = False
        
        if self.today is None:
            
            self.today = datetime.now()
            
        if self.today.weekday() in range(0,6):
            condition = True
            
        else:
            condition = False
        
        return condition

    
condition = TimeCheck()
phonebook=PhoneBook()

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
        os.system('python /home/pi/Documents/Code/ac_alert.py')

def send_ac_alert():
    try:
        alert("ALARM IN AUTOCLAVES" )
        sleep(60*10)
        
    except:
        flash(3)
        pass
        os.system('python /home/pi/Documents/Code/ac_alert.py')
        
ac_alarm_pin = 18
led_pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(ac_alarm_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT, initial=0)

schedule.every(5).seconds.do(flash, 1)

#pi = pigpio.pi()

try:
    #pi.set_glitch_filter(ac_alarm_pin, 1000)
    
    while True:
        
        schedule.run_pending()
        
        if GPIO.input(ac_alarm_pin) == False:
            if condition.check_hours(start=6, end=21) == True and condition.check_days() == True:
                sleep(1.5)
                if GPIO.input(ac_alarm_pin) == False:
                    send_ac_alert() 
                
            if condition.check_hours(start=8, end=21) == True and condition.check_days() == False:
                sleep(1.5)
                if GPIO.input(ac_alarm_pin) == False:
                    send_ac_alert() 
            
            while GPIO.input(ac_alarm_pin) == False:
                sleep(0.01)
               
except KeyboardInterrupt:
    print('Clean up')
    GPIO.cleanup()
        
finally:
    print('Clean up')
    GPIO.cleanup()
            
        
