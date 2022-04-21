import json

from . import sensor_pins

from . import mq_135
from . import motion_sensor
from . import dht_sensor

from . import firebase_connection

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
	if debug:
		prettySensorData = json.dumps(sensorData, indent = 4)
		print(f"Sensor data is : {prettySensorData}")