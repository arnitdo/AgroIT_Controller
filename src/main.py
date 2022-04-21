import json
import time
import gpiozero
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import Adafruit_DHT

# Constants
CREDENTIAL_PATH = "credentials.json"
SMOKE_SENSOR_PIN = 14
MOTION_SENSOR_PIN = 17
MOISTURE_SENSOR_PIN = 23
DHT_SENSOR_PIN = 10

# Firebase credentials
credentialsCertificate = credentials.Certificate(CREDENTIAL_PATH)
firebase_admin.initialize_app(credentialsCertificate)
database = firestore.client()

# Sensor wrapper classes

class MQ135(gpiozero.GPIODevice):
	def __init__(self, pin_no):
		super().__init__(pin_no)

class MoistureSensor(gpiozero.GPIODevice):
	def __init__(self, pin_no):
		super().__init__(pin_no)

# Sensors and variables

mq_135 = MQ135(SMOKE_SENSOR_PIN)
dht_sensor = Adafruit_DHT.DHT11
moisture_sensor = MoistureSensor(MOISTURE_SENSOR_PIN)
motion_sensor = gpiozero.MotionSensor(MOTION_SENSOR_PIN)
last_humidity = 0
last_temperature = 0

# Data functions

def getSmokeValue():
	return mq_135.value

def getMoistureValue():
	return moisture_sensor.value

def getHumidityValue():
	humidity, _ = Adafruit_DHT.read(dht_sensor, DHT_SENSOR_PIN)
	global last_humidity
	if humidity == None:
		humidity = last_humidity
	last_humidity = humidity
	return humidity

def getTemperatureValue():
	_, temperature = Adafruit_DHT.read(dht_sensor, DHT_SENSOR_PIN)
	global last_temperature
	if temperature == None:
		temperature = last_temperature
	last_temperature = temperature
	return temperature

def getMotionValue():
	return motion_sensor.value

def insertData(sensorValues):
	smokeSensor = sensorValues["smokeSensor"]
	motionSensor = sensorValues["motionSensor"]
	moistureSensor = sensorValues["moistureSensor"]
	dhtSensor = sensorValues["dhtSensor"]
	collection = database.collection("sensorData")
	collection.document("smokeSensor").update(smokeSensor)
	collection.document("motionSensor").update(motionSensor)
	collection.document("moistureSensor").update(moistureSensor)
	collection.document("dhtSensor").update(dhtSensor)

def generateJSONData():
	return {
		"smokeSensor" : {
			"smokeValue" : getSmokeValue(debug)
		},
		"motionSensor" : {
			"motionValue" : getMotionValue(debug)
		},
			"moistureSensor" : {
			"moistureValue" : getMoistureValue(debug)
		},
		"dhtSensor" : {
			"humidityValue" : getHumidityValue(debug),
			"temperatureValue" : getTemperatureValue(debug)
		}
	}

def main():
	while True:
		sensorData = generateJSONData()
		print(
			json.dumps(
				sensorData, indent = 4
			)
		)
		insertData(sensorData)
		time.sleep(5)

if __name___ == "__main__":
	main()