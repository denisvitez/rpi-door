import paho.mqtt.client as mqtt
import time
import RPi.GPIO as GPIO

busy = False
def setupPin(pinNumber):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pinNumber, GPIO.OUT)

def pinOn(pinNumber):
	GPIO.output(pinNumber, 1)

def pinOff(pinNumber):
	GPIO.output(pinNumber, 0)

def openDoor(pinNumber):
	global busy
	if not busy:
		busy = True
		print "Opening door..."
		pinOn(pinNumber)
		time.sleep(0.2)
		#time.sleep(5)
		pinOff(pinNumber)
		print "Door opened..."
		busy = False
	else:
		print "Doors are busy"

def on_connect(client, userdata, rc):
	client.subscribe("RPI/door")
	print "Subscribed to topic RPI/door"

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	global pin
        print "Topic: ", msg.topic+"\nMessage: "+str(msg.payload)
	openDoor(pin)
	print "Waiting for input..."
	
pin = 4
setupPin(pin)
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

