from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_string("""
<SplashScreen1>:
    name: 'splash_screen1'
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1  # White background color
            Rectangle:
                pos: self.pos
                size: self.size
        Image:
            source: 'a.png'

""")

class SplashScreen1(Screen):
    def on_enter(self, *args):
        Clock.schedule_once(self.switch_to_main_screen,6)  # Switch to main screen after 2 seconds
    def switch_to_main_screen(self, *args):
        self.manager.current = 'splash_screen2'