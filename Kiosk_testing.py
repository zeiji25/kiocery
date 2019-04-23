from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
available_ports = ["HelloWorld"]
for p in ports:
    available_ports.append(p.device)


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Username:"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text="Password:"))
        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)

        self.add_widget(Label(text="Two Factor Authentication:"))
        self.tfa = TextInput(multiline=False)
        self.add_widget(self.tfa)


class SimpleKivy(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    SimpleKivy().run()
