import random
import time
import json

def getValueMap():
    """ sensor measurement implementation"""
    readings = random.random()*100
    timestamp = int(time.time())
    ht = {"readings": readings, "timestamp":timestamp, "note": "random reader"}
    hts = json.dumps(ht)
    print hts
    return ht