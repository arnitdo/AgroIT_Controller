import sensor_pins
import gpiozero
import Adafruit_DHT
import random

dht_sensor = Adafruit_DHT.DHT11
last_humidity = 0
last_temperature = 0

def getHumidityValue(debug = False):
	if debug:
		return random.random()
	humidity, _ = Adafruit_DHT.read(dht_sensor, sensor_pins.DHT_SENSOR_PIN)
	if humidity == None:
		humidity = last_humidity
	last_humidity = humidity
	return humidity

def getTemperatureValue(debug = False):
	if debug:
		return random.random()
	_, temperature = Adafruit_DHT.read(dht_sensor, sensor_pins.DHT_SENSOR_PIN)
	if temperature == None:
		temperature = last_temperature
	last_temperature = temperature
	return temperature