from gpiozero import GPIODevice
import sensor_pins
class MQ135(GPIODevice):
	def __init__(self, pin_no):
		super().__init__(pin_no)

mq_135 = MQ135(sensor_pins.SMOKE_SENSOR_PIN)

def getSmokeValue():
	return mq_135.value