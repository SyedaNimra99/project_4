from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,FadeTransition
from splashscreen1 import SplashScreen1
from splashscreen2 import SplashScreen2
from login import Login
from kivy.core.window import Window
from signup import Signup

Window.size=(320,560)

class Interface(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition=FadeTransition()
        splash1 = SplashScreen1()
        splash2 = SplashScreen2()
        login = Login()
        signup=Signup()
        self.add_widget(splash1)
        self.add_widget(splash2)
        self.add_widget(login)
        self.add_widget(signup)

class MyApp(App):
    def build(self):
        pass

MyApp().run()
