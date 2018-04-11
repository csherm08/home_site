import RPi.GPIO as GPIO
import requests
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)
url='http://localhost:8000/switchStatus'
callback=lambda *a: switchURL()
GPIO.add_event_detect(17, GPIO.FALLING, callback, bouncetime=300)
def switchURL():
   r = requests.post(url)
   print r.content
	
while True:
    input_value = GPIO.input(17)
    if input_value == 'True':
	switchURL()
   	time.sleep(1)

#    time.sleep(0.2)
#    if GPIO.input(17) == True: # Listen for the press, the loop until it steps
#        print "Started press"
#        while GPIO.input(17) == True:
#            time.sleep(0.5)
#    r = requests.post(url)
#    print r.content

