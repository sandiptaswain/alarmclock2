
from tkinter.ttk import*
from tkinter import*
from pygame import mixer
from datetime import datetime
from time import sleep

#window
window=Tk()
window.title()
window.geometry('350x150')
def sound_alarm():
    mixer.music.load("alarm.mp3")
    mixer.music.play()

def alarm():
    while True:
        control=1
        print(control)

        alarm_hour="08"
        alarm_minute="32"
        alarm_seconds="00"
        alarm_period="PM".upper()

        now=datetime.now()

        hour=now.strftime("%I")
        minute=now.strftime("%M")
        seconds=now.strftime("%S")
        periods=now.strftime("%p")

        if control==1:
            if alarm_period==periods:
                if alarm_hour==hour:
                    if alarm_minute==minute:
                        if alarm_seconds==seconds:

                            print("Time to take break")
                            sound_alarm()

        sleep(1)

mixer.init()
alarm()
window.mainloop()