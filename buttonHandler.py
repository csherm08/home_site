import RPi.GPIO as gpio
import requests
import time

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.IN, pull_up_down=gpio.PUD_UP)
url='http://localhost:8000/switchStatus'
print("Listening for press")
def switchURL(ev=None):
   print(gpio.input(17))
   r = requests.post(url)
   time.sleep(0.4)
   #print r.content
	

gpio.add_event_detect(17, gpio.FALLING, callback=switchURL, bouncetime=300)
def loop():
    while True:
	pass
#while True:
#    input_value = gpio.input(17)
#    if input_value == False:
#        print('The button has been pressed...')
#        while input_value == False:
#            input_value = gpio.input(17)
#    time.sleep(0.2)
#    if GPIO.input(17) == True: # Listen for the press, the loop until it steps
#        print "Started press"
#        while GPIO.input(17) == True:
#            time.sleep(0.5)
#    r = requests.post(url)
#    print r.content
if __name__ == '__main__': 
	loop()
