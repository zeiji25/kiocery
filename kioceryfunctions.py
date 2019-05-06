import serial
import serial.tools.list_ports
import binascii
import time
import re
import mysql.connector
from mysql.connector import MySQLConnection, Error



def rfid_connect():   # Connect RFID
    try:
        baud = 9600
        ser = serial.Serial('/dev/ttyUSB0', baud, timeout= 0.2)
        if ser.isOpen():
            print(ser.name + ' is open...')
            ser.write(serial.to_bytes([0x7C, 0xFF, 0xFF, 0x82, 0x32, 0x00, 0xD2]))
            response = binascii.hexlify(ser.readline())
            response = str(response, 'UTF8')
            print(response)
            if response == device_check:
                print("RFID Properly Initialized")
def rfid_disconnect(): # Disconnect RFID
    try:
        print("Program Closing")
        time.sleep(2)
        ser.close()
        print('closed')

def scan(): # Disconnect RFID
    try:
        tags = []
        for x in range(0, 15, 1):
            ser.write(serial.to_bytes([0x7C, 0xFF, 0xFF, 0x11, 0x32, 0x00, 0x43]))
            response = binascii.hexlify(ser.readline())
            response = str(response, 'UTF8')
            for i in range(14, len(response), 28):
                tags.append(response[i+2:i+26])
                tags = filter(None, tags)
                tags = list(set(tags))
                tags.sort()
            print(tags)
        print(len(tags))
    except Exception as e:
        print(e)
