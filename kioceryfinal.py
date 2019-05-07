import serial
import serial.tools.list_ports
import binascii
import time
import re
import mysql.connector
from itertools import groupby
import os
os.environ['KIVY_VIDEO'] = 'ffpyplayer'
from mysql.connector import MySQLConnection, Error
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.videoplayer import VideoPlayer
from kivy.core.image import zipfile
from kivy.uix.video import Video
from kivy.uix.scatter import Scatter
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
Window.maximize()
tags = []
response = []
final = []

#baud = 9600
#ser = serial.Serial('COM7', baud, timeout= 0.2)
#if ser.isOpen():
#    print(ser.name + ' is open...')
#    ser.write(serial.to_bytes([0x7C, 0xFF, 0xFF, 0x82, 0x32, 0x00, 0xD2]))
#    response = binascii.hexlify(ser.read(41))
#    response = str(response, 'UTF8')
#    print(response)
#    print("RFID Properly Initialized")

def scan(self): # Disconnect RFID
        global tags, response, final
        def regs(list):
            regex_string = re.findall(r'(?<=01)30\d{22}(?=b)' , list)
            return regex_string
        for x in range(0, 15, 1):
            ser.write(serial.to_bytes([0x7C, 0xFF, 0xFF, 0x11, 0x32, 0x00, 0x43]))
            response = binascii.hexlify(ser.readline())
            response = str(response, 'UTF8')
            reduc = regs(response)
            tags = list(set(tags).union(set(reduc)))
        print('\n\n')
        tags.sort()
        print(tags)
        print(len(tags))

class MainScreen(Screen):
    pass

class POS(Screen):
    pass

class ScreenManagement(ScreenManager):
    def scan(self): # Disconnect RFID
            global tags, response, final
            def regs(list):
                regex_string = re.findall(r'(?<=01)30\d{22}(?=b)' , list)
                return regex_string
            for x in range(0, 15, 1):
                ser.write(serial.to_bytes([0x7C, 0xFF, 0xFF, 0x11, 0x32, 0x00, 0x43]))
                response = binascii.hexlify(ser.readline())
                response = str(response, 'UTF8')
                reduc = regs(response)
                tags = list(set(tags).union(set(reduc)))
            print('\n\n')
            tags.sort()
            print(tags)
            print(len(tags))
    pass


presentation = Builder.load_file("kiocery.kv")

class MainApp(App):
    def build(self):
        return presentation

MainApp().run()
