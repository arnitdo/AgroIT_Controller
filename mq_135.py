from gpiozero import GPIODevice

class MQ135(GPIODevice):
	def __init__(self, pin_no):
		super().__init__(pin_no)

