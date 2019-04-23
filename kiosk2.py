import serial
import serial.tools.list_ports
import binascii
import time
import re
import mysql.connector
from mysql.connector import MySQLConnection, Error

ports = serial.tools.list_ports.comports()
available_ports = []
for p in ports:
    available_ports.append(p.device)

device_check = "ccffff8200220a207777772e416f7369642e636f6d200a205056332e36384e6f2e3a0036353533358c"
rf_config = "ccffff81001c1e0078545d666f7882030a0201001e0a0f0f20020102000200000032d4"


while True:
    print("Choose from the following Commands\n")
    print("1  Connect\n2  Terminate\n3  Scan\n")
    cmd = input("Enter command:  ")
    if cmd == "2":
        print("Program Closing")
        time.sleep(2)
        ser.close()
        print('closed')
        break
    elif cmd == "1":
        print('Choose from the available ports\n')
        print(available_ports)
        port = input('\nWhat port will you use?\n')
        if (port not in available_ports) == False:
            baud = 9600
            ser = serial.Serial(port, baud, timeout=.5)
            if ser.isOpen():
                print(ser.name + ' is open...')
                ser.write(serial.to_bytes([0x7C, 0xFF, 0xFF, 0x82, 0x32, 0x00, 0xD2]))
                response = binascii.hexlify(ser.readline())
                response = str(response, 'UTF8')
                print(response)
                if response == device_check:
                    print("RFID Properly Initialized")
                    print("Checking Reader Configuration")
                    ser.write(serial.to_bytes([0x7C, 0xFF, 0xFF, 0x81, 0x32, 0x00, 0xD3]))
                    config = binascii.hexlify(ser.read(35))
                    config = str(config, 'UTF8')
                    print(config)
                    if config == rf_config:
                        print("RFID Configuration is Correct")
        else:
            print("\n\n\nPort not available Try Again\n\n\n\n")
    elif cmd == '3':
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
        for y in range(0, len(tags), 1):
            tags[y] = bytearray.fromhex(tags[y]).decode()
        print(tags)
        distrib = [len(list(group)) for key, group in groupby(tags)]
        print(distrib)
exit()
