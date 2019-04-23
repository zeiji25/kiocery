import serial
import serial.tools.list_ports
import binascii
from time import sleep
import re
import mysql.connector
from mysql.connector import MySQLConnection, Error
from itertools import groupby


ports = serial.tools.list_ports.comports()
available_ports = []
for p in ports:
    available_ports.append(p.device)

device_check = "ccffff8200220a207777772e416f7369642e636f6d200a205056332e36384e6f2e3a0036353533358c"
rf_config = "ccffff81001c1e0078545d666f7882030a0201001e0a0f0f20020102000200000032d4"
ser = serial.Serial("COM5", 9600, timeout=.5)
ser.write(serial.to_bytes([0x7C, 0xFF, 0xFF, 0x82, 0x32, 0x00, 0xD2]))
response = binascii.hexlify(ser.read(41))
response = str(response, 'UTF8')
print(response)
tags = []
for x in range(0, 100, 1):
    ser.write(serial.to_bytes([0x7C, 0xFF, 0xFF, 0x11, 0x32, 0x00, 0x43]))
    response = binascii.hexlify(ser.readline())
    sleep(.010)
    response = str(response, 'UTF8')
    print(response)
    sleep(.1)
    for i in range(14, len(response), 100):
        tags.append(response[i+2:i+26])
        tags.sort()
        print(tags)
    sleep(.010)
print(len(tags))
distrib = [len(list(group)) for key, group in groupby(tags)]
print(distrib)
print("Program Closing")
sleep(2)
ser.close()
print('closed')
