from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen


class PongGame(Screen):
    pass


class PongApp(App):
    def build(self):
        return PongGame()


if __name__ == '__main__':
    PongApp().run()
