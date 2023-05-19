import pyautogui as pg
import RPi.GPIO as GPIO			# using Rpi.GPIO module
from time import sleep			# import function sleep for delay
GPIO.setmode(GPIO.BCM)			# GPIO numbering
GPIO.setwarnings(False)			# enable warning from GPIO
AN2 = 25			# set pwm2 pin on MD10-Hat
AN1 = 24			# set pwm1 pin on MD10-hat
DIG2 = 23				# set dir2 pin on MD10-Hat
DIG1 = 18				# set dir1 pin on MD10-Hat
GPIO.setup(AN2, GPIO.OUT)		# set pin as output
GPIO.setup(AN1, GPIO.OUT)		# set pin as output
GPIO.setup(DIG2, GPIO.OUT)		# set pin as output
GPIO.setup(DIG1, GPIO.OUT)		# set pin as output
sleep(1)				# delay for 1 seconds
p1 = GPIO.PWM(AN1, 100)		# set pwm for M1
p2 = GPIO.PWM(AN2, 100)		# set pwm for M2


try:
	while True:
		if pg.press('up'):
			GPIO.output(DIG1, GPIO.LOW)		# set AN1 as HIGH, M1B will turn ON
			GPIO.output(DIG2, GPIO.LOW)		# set AN2 as HIGH, M2B will turn ON
			p1.start(100)				# set Direction for M1
			p2.start(100)
			print("UP")
			sleep(1)				# set Direction for M2
		
except:					# exit programe when keyboard interupt
   p1.start(0)				# set speed to 0
   p2.start(0)	
   
   GPIO.cleanup() 			# set speed to 0
					# Control+X to save and exit
		 
