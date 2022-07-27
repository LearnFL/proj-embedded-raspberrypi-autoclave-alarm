This software sends text messages via TWILIO when analog equipment triggers an alarm.

ac_alarm.py sends a text message when an analog alarm bell goes off. You may set time and day of the week limitations for the text messages.
10 minutes must pass before another text message may be sent. The system will sleep for as long as the triggering event is active, so you the user 
will not be getting a new message every 10 minutes.

power_alert.py sends a text message when the power goes out, for this reason the development board must be on UPS.
There is no time or day of the week limitation for this alarm.

connection_check.py checks whether the system has internet connection.

I used raspberry pi 4 which autostarts code when it is plugged in.

![560A3C71-73EE-4EDF-917E-D10F73D2DBBE](https://user-images.githubusercontent.com/86169204/181386531-37d6fc93-5f81-4d67-a373-1ccb4cf7a965.JPEG)
