from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_string("""
#: import CButton custom_widgets
#: import CTextInput custom_widgets

<Signup>:
    name:"signup"
    BoxLayout:
        orientation: "vertical"
        padding:dp(20)
        BoxLayout:
            size_hint:1,0.4
            Image:
                source: "a.png" 
        AnchorLayout:
            size_hint:1,0.6
            anchor_y:"top"      
            BoxLayout:
                orientation: "vertical"
                size_hint_y:None
                height:self.minimum_height
                spacing:dp(10)
                Label:
                    text: "Create your Account"
                    color:0,0,0,1
                    padding: [0,0,0,dp(10)]
                    font_name:"robotoblack.ttf"
                    halign: "left"
                    text_size:self.size
                CTextInput:
                    hint_text: "Email"
                    size_hint_y:None
                    height: dp(50)
                CTextInput:
                    hint_text: "Password"
                    size_hint_y:None
                    height: dp(50)
                CTextInput:
                    hint_text: "Confirm Password"
                    size_hint_y:None
                    height: dp(50)
                CButton:
                    text: "Signup"
                    size_hint_y:None
                    height: dp(50)
                    
""")

class Signup(Screen):
    pass
