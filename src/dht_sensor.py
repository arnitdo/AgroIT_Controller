from . import sensor_pins
import gpiozero
import adafruit_dht

dht_sensor = adafruit_dht.DHT11
humidity, temperature = adafruit_dht.read_retry(dht_sensor, sensor_pins.DHT_SENSOR_PIN)

def getHumidityValue():
	humidity, _ = adafruit_dht.read_retry(dht_sensor, sensor_pins.DHT_SENSOR_PIN)
	return humidity

def getTemperatureValue():
	_, temperature = adafruit_dht.read_retry(dht_sensor, sensor_pins.MOISTURE_SENSOR_PIN)
	return temperature