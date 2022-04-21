import json

import sensor_pins
import mq_135
import motion_sensor
import dht_sensor
import moisture_sensor

import firebase_connection

DEBUG = True
def generateJSONData():
	return {
		"sensorData" : {
			"smokeSensor" : {
				"smokeValue" : mq_135.getSmokeValue()
			},
			"motionSensor" : {

				"motionValue" : motion_sensor.getMotionValue()
			},
			"moistureSensor" : {
				"moistureValue" : moisture_sensor.getMoistureValue()
			},
			"dhtSensor" : {
				"humidityValue" : dht_sensor.getHumidityValue(),
				"temperatureValue" : dht_sensor.getTemperatureValue()
			}
		}
	}

while True:
	sensorData = generateJSONData()
	if DEBUG:
		prettySensorData = json.dumps(sensorData, indent = 4)
		print(f"Sensor data is : {prettySensorData}")