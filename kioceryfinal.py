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
    except Error as e:
        print(e)

def rfid_disconnect(): # Disconnect RFID
    try:
        print("Program Closing")
        time.sleep(2)
        ser.close()
        print('closed')
        break
    except Error as e:
        print(e)

def scan(): # Disconnect RFID
    try:
        pass
    except Exception as e:
        raise
