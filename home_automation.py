import Rpi.GPIO as GPIO
import time
import firebase as firebase
dev1=7
dev2=11
ac=13
GPIO.setmode(GPIO.BOARD)
GPIO.setup(dev1,GPIO.OUT)
GPIO.setup(dev2,GPIO.OUT)
GPIO.setup(ac,GPIO.OUT)
firebase=firebase.FirebaseApplication('https://finalproject-3546d.firebaseio.com/',None)
while True:
    device1=firebase.get('device1on',None)
    device2=firebase.get('device2on',None)
    ac_on=firebase.get('ac',None)
    if device1==2:
        GPIO.output(dev1,1)
    if device2==3:
        GPIO.output(dev2,1)
    if ac_on==10:
        GPIO.output(ac,1)
    if device1==0:
        GPIO.output(dev1,0)
    if device2==1:
        GPIO.output(dev2,0)
    if ac_on==8:
        GPIO.output(ac,0)
GPIO.cleanup()
