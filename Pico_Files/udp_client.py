from networking import connect
import socket
from time import sleep
from uosc.client import create_message

from machine import I2C, Pin
import time
import math
from bno08x_i2c import *

I2C1_SDA = Pin(2)
I2C1_SCL = Pin(3)

i2c1 = I2C(1, scl=I2C1_SCL, sda=I2C1_SDA, freq=100000, timeout=200000 )
print("I2C Device found at address : ",i2c1.scan(),"\n")

bno = BNO08X_I2C(i2c1, debug=False)
print("BNO08x I2C connection : Done\n")

bno.enable_feature(BNO_REPORT_ACCELEROMETER)
bno.enable_feature(BNO_REPORT_MAGNETOMETER)
bno.enable_feature(BNO_REPORT_GYROSCOPE)
bno.enable_feature(BNO_REPORT_ROTATION_VECTOR)




#network connect
connect()
# The target IP and port you want to send the UDP packet to
udp_ip = '192.168.1.203'  # Change to the IP of the target device
udp_port = 1337  # Change to the target port

# Create a socket for UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect((udp_ip,udp_port))
    

while True:
    x,y,z = bno.acceleration
    message=create_message('/accelXYZ',x,y,z)
    sock.send(message)
    x,y,z = bno.gyro
    message=create_message('/GyroXYZ',x,y,z)
    sock.send(message)
    x,y,z = bno.magnetic
    message=create_message('/MagXYZ',x,y,z)
    sock.send(message)
    qi, qj, qk, qr = bno.quaternion
    message=create_message('/QuatIJKR', qi,qj,qk,qr)
    sock.send(message)
    sleep(0.1)
    