import serial
import serial.tools.list_ports
import binascii

ports = serial.tools.list_ports.comports()
available_ports = []
for p in ports:
    available_ports.append(p.device)


while True:
    cmd = input("Enter command")
    print(cmd)
    if cmd == 'terminate':
        ser.close()
        print('closed')
        break
    elif cmd == 'connect':
        print('Choose from the available ports')
        print(available_ports)
        port = input('What port will you use?')
        if (port not in available_ports) == False:
            baud = 9600
            ser = serial.Serial(port, baud, timeout=None)
            if ser.isOpen():
                print(ser.name + ' is open...')
        else:
            exit()
    elif cmd == 'initialize':
        ser.write(serial.to_bytes([0x7C, 0xFF, 0xFF, 0x82, 0x32, 0x00, 0xD2]))
        response = ser.read(41)
        print(binascii.hexlify(response))
    elif cmd == "rfidscan":
        ser.write(serial.to_bytes([0x7C, 0xFF, 0xFF, 0x12, 0x32, 0x03, 0x01, 0x02, 0x03, 0x39]))
        response = ser.read(20)
        print(response)
    else:
        print('Invalid Command')
exit()
