import sensor_pins
import gpiozero
import Adafruit_DHT
import random

dht_sensor = Adafruit_DHT.DHT11

def getHumidityValue(debug = False):
	if debug:
		return random.random()
	humidity, _ = Adafruit_DHT.read_retry(dht_sensor, sensor_pins.DHT_SENSOR_PIN)
	return humidity

def getTemperatureValue(debug = False):
	if debug:
		return random.random()
	_, temperature = Adafruit_DHT.read_retry(dht_sensor, sensor_pins.MOISTURE_SENSOR_PIN)
	return temperature