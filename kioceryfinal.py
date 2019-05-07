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
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.recycleview import RecycleView
from kivy.config import Config

Window.maximize()
totaltags = [1,2,3,4,5,6,7,8]
response = []
final = []
sortedtags = []
distrib = []

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
        global totaltags, response, final, sortedtags, distrib
        def regs(list):
            regex_string = re.findall(r'(?<=01)30\d{22}(?=b)' , list)
            return regex_string
        for x in range(0, 15, 1):
            ser.write(serial.to_bytes([0x7C, 0xFF, 0xFF, 0x11, 0x32, 0x00, 0x43]))
            response = binascii.hexlify(ser.readline())
            response = str(response, 'UTF8')
            reduc = regs(response)
            totaltags.extend(reduc)
            sortedtags.sort(list(set(c).union(set(b))))
            distrib = [len(list(group)) for key, group in groupby(totatags)]
        print('\n\n')
        print(len(sortedtags))
        print(len(distrib))

class MyPopupProgressBar(Widget):

    progress_bar = ObjectProperty() # Kivy properties classes are used when you create an EventDispatcher.

    def __init__(self, **kwa):
        super(MyPopupProgressBar, self).__init__(**kwa) #super combines and initializes two widgets Popup and ProgressBar
        self.progress_bar = ProgressBar() # instance of ProgressBar created.
        self.popup = Popup(title='Scanning', content=self.progress_bar) # progress bar assigned to popup
        self.popup.bind(on_open=self.puopen) # Binds super widget to on_open.
        Clock.schedule_once(self.progress_bar_start) # Uses clock to call progress_bar_start() (callback) one time only

    def progress_bar_start(self, instance): # Provides initial value of of progress bar and lanches popup
        self.progress_bar.value = 1 # Initial value of progress_bar
        self.popup.size_hint = (.5,.5)
        self.popup.open() # starts puopen()

    def next(self, dt): # Updates Project Bar
        if self.progress_bar.value >= 100: # Checks to see if progress_bar.value has met 100
            self.popup.dismiss()
            return False # Returning False schedule is canceled and won't repeat
        self.progress_bar.value += 2 # Updates progress_bar's progress

    def puopen(self, instance): # Called from bind.
        Clock.schedule_interval(self.next, .0005) # Creates Clock event scheduling next() every 5-1000th of a second.


class MainScreen(Screen):
    pass

class POS(Screen):
    # def __init__(self, **kwargs):
    #     super(POS, self).__init__(**kwargs)
    #     # assigning data in RecyclerView
    #     global totaltags, response, final, sortedtags, distrib
    #     totaltags = ['1','2','3','4','5','6','7','8']
    #     self.data = [{'text': totaltags(x)} for x in range(100)]
    pass
class Receipt(Screen):
    pass

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        global totaltags, response, final, sortedtags, distrib

        self.data = [{'text': totaltags(x)} for x in range(10)]

class ScreenManagement(ScreenManager):
    def scan(self): # Disconnect RFID
            global totaltags, response, final, sortedtags, distrib
            def regs(list):
                regex_string = re.findall(r'(?<=01)30\d{22}(?=b)' , list)
                return regex_string
            for x in range(0, 15, 1):
                ser.write(serial.to_bytes([0x7C, 0xFF, 0xFF, 0x11, 0x32, 0x00, 0x43]))
                response = binascii.hexlify(ser.readline())
                response = str(response, 'UTF8')
                reduc = regs(response)
                totaltags.extend(reduc)
                totaltags.sort()
                sortedtags = list(set(totaltags).union(set(reduc)))
                sortedtags.sort()
                distrib = [len(list(group)) for key, group in groupby(totaltags)]
            print('\n\n')
            print(totaltags)
            print(sortedtags)
            print(len(sortedtags))
            print(len(distrib))
    pass

presentation = Builder.load_file("kiocery.kv")

class MainApp(App):
    def build(self):
        return presentation

MainApp().run()
