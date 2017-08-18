#MODULE TEST FOR ULTRASONIC DISTANCE SENSOR HC-SR04
#''''''''''''''''''''''''''''''''''''''''''''''''''

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 12
ECHO = 16

GPIO.setup(TRIG,GPIO.OUT)
GPIO.output(TRIG,0)

GPIO.setup(ECHO,GPIO.IN)

#Sensor needs a short delay to settle. Specification suggested a 50ms cycle time. So we use 100ms.
time.sleep(0.1)

print "Starting measurement..."

#send a short signal to ultrasound module (10 microseconds as specified before)
GPIO.output(TRIG,1)
time.sleep(0.00001)
GPIO.output(TRIG,0)

#next we need to listen to the echo pin and be as efficient as possible with the code because this happens incredibly fast.
while GPIO.input(EHCO) == 0:
	pass
start = time.time()

while GPIO.input(EHCO) == 1:
	pass
stop = time.time()

#time.time() expresses the current time in seconds. we record two times. at the beginning and at the end of the pulse.

#----EXPLANATION IN FINNISH----
#    ylläoleva koodi toimii näin: while loop jatkuu niin kauan kunnes ECHO-pinni ottaa vastaan inputtia,
#    jollon silmukan ehto muuttuu epätodeksi ja silmukka sulkeutuu. nauhoitetaan aloitusaika.
#    alkaa uusi silmukka joka kestää niin kauan kun ECHO-pinni ottaa vastaan inputtia (signaalia = 1 = true),
#    kun signaali päättyy (input palaa 0:ksi / false), silmukka sulkeutuu ja nauhoitetaan lopetusaika.

print (stop - start) * 17000

#print the distance in centimeters. 
#    Speed of sound is 340m/s and distance is 2d so we divide 340 by two, 
#    and multiply it with 100 to get the answer in centimeters instead of meters.
#    distance = time x speed.

GPIO.cleanup()
