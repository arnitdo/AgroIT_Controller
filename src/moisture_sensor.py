import gpiozero
import sensor_pins

import random

class MoistureSensor(gpiozero.GPIODevice):
	def __init__(self, pin_no):
		super().__init__(pin_no)
	
moisture_sensor = MoistureSensor(sensor_pins.MOISTURE_SENSOR_PIN)

def getMoistureValue():
	if DEBUG:
		return random.random()
	return moisture_sensor.value