import gpiozero
import sensor_pins

import random

class MQ135(gpiozero.GPIODevice):
	def __init__(self, pin_no):
		super().__init__(pin_no)

mq_135 = MQ135(sensor_pins.SMOKE_SENSOR_PIN)

def getSmokeValue():
	if DEBUG:
		return random.random()
	return mq_135.value