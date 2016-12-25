import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

def setupPin(pinNumber):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pinNumber, GPIO.IN)

mqttc = mqtt.Client("physical_button")
mqttc.connect("localhost", 1883)

pin = 15 
setupPin(pin)
time.sleep(10)
while True:
	if (GPIO.input(pin)):
		print "Button pressed..."
		mqttc.publish("RPI/door", 1)
		mqttc.loop(2)
		time.sleep(5)
	time.sleep(0.5)

