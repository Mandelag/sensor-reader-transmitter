import time
import json
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 18
GPIO_ECHO = 23

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    distance = None
    GPIO.output(GPIO_TRIGGER, False)
    time.sleep(0.05)
    
    GPIO.output(GPIO_TRIGGER, True)
    for i in range(0,2):
        pass
    #time.sleep(0.0001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time()
        
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
        
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime

    distance = (TimeElapsed * 34300) / 2.0
    return distance

def getValue():
    ds = None
    try:
        ds = distance()
    finally:
        pass
        #GPIO.cleanup()
    timestamp = int(time.time())
    ht = {"distance": ds, "timestamp":timestamp}
    hts = json.dumps(ht)
    print hts
    if ds is not None:
        return ((ds, "f"), (timestamp, "i"))
    else:
        raise ValueError

def getValueMap():
    ds = None
    try:
        ds = distance()
    finally:
        pass
        #GPIO.cleanup()
    timestamp = int(time.time())
    ht = {"distance": ds, "timestamp":timestamp}
    hts = json.dumps(ht)
    print hts
    if ds is not None:
        return ht
    else:
        raise ValueError
        
def getSensorMetadata():
    """ temporarily hardcode the metadata """
    metadata = {
        "sensor_name":"HC-SR04"
    }
    return metadata
        