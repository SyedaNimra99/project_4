from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_string("""
<SplashScreen2>:
    name: 'splash_screen2'
    BoxLayout:
        orientation: 'vertical'
        Image:
            source: 'b.png'  # Replace with the path to your image
            allow_stretch: True
            keep_ratio: False
            size_hint: (1, 1)
                    
""")

class SplashScreen2(Screen):
    def on_enter(self, *args):
        Clock.schedule_once(self.switch_to_main_screen1,2)  # Switch to main screen after 2 seconds
    def switch_to_main_screen1(self, *args):
        self.manager.current = 'interface'