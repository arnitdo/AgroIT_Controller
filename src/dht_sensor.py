import sensor_pins
import gpiozero
import Adafruit_DHT

dht_sensor = Adafruit_DHT.DHT11
humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, sensor_pins.DHT_SENSOR_PIN)

def getHumidityValue():
	humidity, _ = Adafruit_DHT.read_retry(dht_sensor, sensor_pins.DHT_SENSOR_PIN)
	return humidity

def getTemperatureValue():
	_, temperature = Adafruit_DHT.read_retry(dht_sensor, sensor_pins.MOISTURE_SENSOR_PIN)
	return temperature