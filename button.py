import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

def setupPin(pinNumber):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pinNumber, GPIO.IN, pull_up_down=GPIO.PUD_UP)

mqttc = mqtt.Client("physical_button")
mqttc.connect("localhost", 1883)

pin = 17 
setupPin(pin)
print "Waiting for pin to setup..."
time.sleep(10)
while True:
	try:
		if GPIO.input(pin) == False:
			print "Button pressed..."
			mqttc.publish("RPI/door", 1)
			mqttc.loop(2)
			time.sleep(5)
	except:
		print "Exception occured while pressing button..."

