import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT) # Servo signal
GPIO.setup(12,GPIO.OUT)	# Buzzer
GPIO.setup(16,GPIO.IN) 	# IR sensor
pwm = GPIO.PWM(18,50)

def open_gate():
	pwm.start(11)
	print('Gate is open')
	while GPIO.input(16)== False:
		x=1
	pwm.ChangeDutyCycle(6.5)
	print('Gate is close')
	time.sleep(1)

def buzzer():
	for i in range(5):
		GPIO.output(12,GPIO.HIGH)
		time.sleep(.5)
		GPIO.output(12,GPIO.LOW)
		time.sleep(.5)
