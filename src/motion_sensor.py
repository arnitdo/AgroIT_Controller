import gpiozero
import sensor_pins

motion_sensor = gpiozero.MotionSensor(sensor_pins.MOTION_SENSOR_PIN)

def getMotionValue():
	return motion_sensor.value