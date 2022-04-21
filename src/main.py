
DEBUG = True

import json
import time

import sensor_pins
import mq_135
import motion_sensor
import dht_sensor
import moisture_sensor

import firebase_connection

def generateJSONData(debug = False):
	return {
		"sensorData" : {
			"smokeSensor" : {
				"smokeValue" : mq_135.getSmokeValue(debug)
			},
			"motionSensor" : {

				"motionValue" : motion_sensor.getMotionValue(debug)
			},
			"moistureSensor" : {
				"moistureValue" : moisture_sensor.getMoistureValue(debug)
			},
			"dhtSensor" : {
				"humidityValue" : dht_sensor.getHumidityValue(debug),
				"temperatureValue" : dht_sensor.getTemperatureValue(debug)
			}
		}
	}

while True:
	sensorData = generateJSONData(DEBUG)
	if debug:
		prettySensorData = json.dumps(sensorData, indent = 4)
		print(f"Sensor data is : {prettySensorData}")

	time.sleep(5)