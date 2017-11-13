import socket
import sys
import struct
from importlib import import_module
import time
import json

def getUTF(string):
    """ not implemented completely yet """
    data = ""
    utf8 = string.encode('utf-8')
    length = len(utf8)
    data = data + struct.pack('!H', length)
    format = '!' + str(length) + 's'
    data = data + struct.pack(format, utf8)
    return data
    
def main():
    if len(sys.argv) < 5:
        print "Usage: python DatagramSender <unique_id> <x> <y> <reader_class> <dst_ip> <dst_port>"
        raise Exception
    ID, X, Y, CLASS, HOST, PORT = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], int(sys.argv[6])
    
    try:
        X = float(X)
        Y = float(Y)
        
        xval = lambda: X
        yval = lambda: Y
        
    except Exception as e:
        xval = lambda : random.random()*360-180
        yval = lambda : random.random()*180-90
        print e
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        try:
            sensor = import_module(CLASS)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
            
            while True:
                try:
                    hostname = socket.gethostname()
                    sensorInfo = {"id":ID, "hostname":socket.gethostname(), "ip_address":socket.gethostbyname(socket.gethostname())}
                    sensorData = sensor.getValueMap()
                    result = {"sensorInfo":sensorInfo, "sensorData":sensorData, "x":xval(), "y":yval()}
                    
                    message = "HELLOSENSOR".encode("UTF-8")
                    message = message + json.dumps(result).encode("UTF-8")
                    sock.sendto(message, (HOST, PORT))
                    time.sleep(0.5)
                    
                except ValueError:
                    print "Cannot get readings."
        except Exception as e:
            print "Exception awe"+str(e)
            time.sleep(60)
            pass
        finally:
            pass

if __name__ == "__main__":
    main()
