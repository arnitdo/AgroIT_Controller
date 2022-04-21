import gpiozero
import sensor_pins

import random

class MoistureSensor(gpiozero.GPIODevice):
	def __init__(self, pin_no):
		super().__init__(pin_no)
	
moisture_sensor = MoistureSensor(sensor_pins.MOISTURE_SENSOR_PIN)

def getMoistureValue(debug = False):
	if debug:
		return random.random()
	moisture_value = moisture_sensor.value
	moisture_value = [1, 0][moisture_value]
	return moisture_sensor.value