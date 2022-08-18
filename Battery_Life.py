#!/usr/bin/env python3

#import modules

from plyer import notification
import psutil

#returns a tuple
battery = psutil.sensors_battery()

plugged = battery.power_plugged

title = ""

Message = ""
#description of code
if __name__=="__main__":
    if plugged:
        percent = battery.percent
        if percent <= 80:
            notification.notify(
            #title of notification
            title = "Plugged In",

            #message of notification
            message=" For better battery life, charge upto 80%" ,

            # displaying time
            timeout=2)
            print (title)


        elif percent == 100:
            notification.notify()
            title =  "Plugged In, "
            message= "Please plugged out the charger. Battery is charged"
            timeout=2
            notification.send()
            ## print (title + message)


        else :
            notification.notify(
            title = "Plugged In",
            message=" Remove the charger please. For better battery life charge up to 80%" ,
            timeout=2)
            print (title)


    else:
        percent = battery.percent
        if percent <=20:
            notification.notify(
            title = "Battery Reminder",
            message="Your battery is running low. You might want to plug in your PC " ,
            timeout=2)
            print (title)

        elif percent <=50:
            notification.notify(
            title = "Battery Reminder",
            message=f" Battery is {percent}." ,
            timeout=2)
            print (title)

        elif percent == 100:
            notification.notify(
            title = "Battery Reminder",
            message="Fully charged" ,
            timeout=2)
            print (title)

        else:
            notification.notify(
            title = "Battery Reminder",
            message=f"Battery is {percent}" ,
            timeout=2)
            print (title)
