import gpiozero
import sensor_pins
import random

motion_sensor = gpiozero.MotionSensor(sensor_pins.MOTION_SENSOR_PIN)

def getMotionValue(debug = False):
	if debug:
		return random.random()
	return motion_sensor.value