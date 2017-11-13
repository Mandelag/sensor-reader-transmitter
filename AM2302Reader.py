import Adafruit_DHT
import time
import json

pin = 3

def getValue():
    """ sensor measurement implementation"""
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302 , pin)
    timestamp = int(time.time())
    ht = {"humidity": humidity, "temperature":temperature, "timestamp":timestamp}
    hts = json.dumps(ht)
    print hts
    if humidity is not None and temperature is not None:
        return ((humidity, "f"), (temperature, "f"), (timestamp, "i"))
    else:
        raise ValueError

def getSensorMetadata():
    """ temporarily hardcode the metadata """
    metadata = {
        "sensor_name":"AM2302"
    }
    return metadata

def getValueMap():
    """ sensor measurement implementation"""
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302 , pin)
    timestamp = int(time.time())
    ht = {"humidity": humidity, "temperature":temperature, "timestamp":timestamp}
    hts = json.dumps(ht)
    print hts
    if humidity is not None and temperature is not None:
        return ht
    else:
        raise ValueError