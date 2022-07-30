# This software sends text messages via TWILIO account when analog equipment triggers an alarm.

## Overview 
I used raspberry pi 4 which autostarts code when it is plugged in.

#### ac_alert.py 
It sends a text message when an analog alarm bell goes off. Instead of a bell you can hoock it. up to soemthing else.
In my case the bell was 110V AC and I could not have directly conected it to the Raspberry Pi. For this reason I used an isolated dry contact relay that i connected to the bell. When the bell activated so did the relay and jumped isolated contacts. When this happened a previously pilled-up Pin on Raspberry Pi went to ground thus triggering code. Another option is to use a buck converter. You woud need to pull a Pin down via a resistor and trigger the code when Pin is HIGH.

You may set time and day of the week limitations for the text messages.
10 minutes must pass before another text message may be sent. The system will sleep for as long as the triggering event is active, so you the user 
will not be getting a new message every 10 minutes.

#### power_alert.py
It sends a text message when the power goes out, for this reason the development board must be on UPS. Your Wi-Fi router neds to be on UPS too unless you have a wired internet.

There is no time or day of the week limitation for this alarm.

#### connection_check.py 
It checks whether the system has internet connection. I bet there should be a better way of doing it. You must check for the internet connection otherwise it defeats the purpose of the system.

## Consideration
You may use GSM board then you will not need internet or TWILIO account.

## Feel free to use and change the code but keep authorship attributes please.

## Screenshots

![560A3C71-73EE-4EDF-917E-D10F73D2DBBE](https://user-images.githubusercontent.com/86169204/181386531-37d6fc93-5f81-4d67-a373-1ccb4cf7a965.JPEG)
