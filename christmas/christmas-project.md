# Notes and TODOs on Improvers Christmas Project

1. Put base scripts onto personal usb stick
* IR sensor base script

``` pir.py
"""
Connect the outer PIR module wires to +(3-5)V and Gnd
Connect the inner PIR module wire to RPi pin 7
"""
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)

try:
    print “PIR Module Test (CTRL+C to exit)”
    time.sleep(2)
    print(“Ready”)
    while True:
        if GPIO.input(PIR_PIN):
        print(“Motion Detected!”)
        time.sleep(1)
except KeyboardInterrupt:
    print(“ Quit”)
    GPIO.cleanup()
```

* Sonar base script
``` sonar.py
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

print("Distance Measurement In Progress")

GPIO.setup(TRIG,GPIO.OUT)

GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG, False)

print("Waiting For Sensor To Settle")

time.sleep(2)

GPIO.output(TRIG, True)

time.sleep(0.00001)

GPIO.output(TRIG, False)
while GPIO.input(ECHO)==0:
    pulse_start = time.time()

while GPIO.input(ECHO)==1:
    pulse_end = time.time()       

pulse_duration = pulse_end - pulse_start
distance = pulse_duration x 17150
distance = round(distance, 2)
print("Distance:",distance,"cm")
GPIO.cleanup()
```

* Motor PWM base script
* LED base script

1. Plan some simple algorithms that the kids can modify 








