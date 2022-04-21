import sensor_pins
import gpiozero
import Adafruit_DHT
import random

dht_sensor = Adafruit_DHT.DHT11

def getHumidityValue():
	if DEBUG:
		return random.random()
	humidity, _ = Adafruit_DHT.read_retry(dht_sensor, sensor_pins.DHT_SENSOR_PIN)
	return humidity

def getTemperatureValue():
	if DEBUG:
		return random.random()
	_, temperature = Adafruit_DHT.read_retry(dht_sensor, sensor_pins.MOISTURE_SENSOR_PIN)
	return temperature