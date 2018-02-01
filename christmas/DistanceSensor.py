from gpiozero import DistanceSensor
from time import sleep
from gpiozero import LED

relay1 = LED(27)
relay2 = LED(24)
relay3 = LED(22)
relay4 = LED(25)
relay5 = LED(23)
#rate=30
#time=1/rate
relay1.off()
relay2.off()
relay3.off()
relay4.off()
relay5.off()
#TODO fix bug, lights stay on when moving out of range during sleep
#
wait_on=0.5
wait_off=0.5

sensor = DistanceSensor(echo=18, trigger=17)
while True:
    distance = sensor.distance * 100
    print('Distance: ', distance)
    print("light")
    relay1.off()
    relay2.off()
    relay3.off()
    relay4.off()
    relay5.off()
    sleep(wait_off)
    #sleep(time)
    if (distance >=0 and distance <=20):
        
        relay1.on()
        relay2.on()
        relay3.on()
        relay4.on()
        relay5.on()
        sleep(wait_on)
        
        sleep(2)

    elif (distance >20 and distance <= 40):
        relay2.on()
        sleep(wait_on)
 
    elif (distance >40 and distance <= 60):
        relay3.on()
        sleep(wait_on)

    elif (distance >60 and  distance <= 80):
        relay4.on()
        sleep(wait_on)

    elif (distance >80 and distance <= 100):
        relay5.on()
        sleep(wait_on)

    
    #add code here

    