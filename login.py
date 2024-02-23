from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_string("""
#: import CButton custom_widgets
#: import CTextInput custom_widgets
#: import SignupText custom_widgets
<Login>:
    name:"interface"
    BoxLayout:
        orientation:"vertical"
        padding:dp(20)
        BoxLayout:
            size_hint:1,0.35 
            Image: 
                source:"a.png"
        AnchorLayout:
            size_hint: 1,0.55
            anchor_y:"top"
            BoxLayout:
                orientation: "vertical"
                size_hint_y:None
                height:self.minimum_height
                spacing: dp(10)
                padding: [dp(10), 0,dp(10), dp(10)]
                Label:
                    text: "Login to your Account"
                    color:0,0,0,1
                    font_zize: "16sp"
                    font_name: "robotoblack.ttf"
                    size_hint_x:None
                    size:self.texture_size
                    halign: "left"
                    padding:[0,0,0,dp(20)]
                CTextInput:
                    size_hint_y:None
                    height: dp(50)
                    multiline: False
                    hint_text: "Email"
                CTextInput: 
                    size_hint_y:None
                    height: dp(50)
                    multiline: False
                    hint_text: "Password"
                CButton:
                    text:"Login"
                    size_hint_y:None
                    height: dp(50)
        AnchorLayout:
            size_hint: 1,0.1
            anchor_x:"center"
            BoxLayout:
                size_hint_x:None
                width:self.minimum_width
                Label:
                    text:"Don't have an account? "
                    color:0,0,0,1
                    size_hint_x:None
                    size:self.texture_size
                SignupText:
                    text:"Signup"
                    size_hint_x:None
                    size:self.texture_size 
                    on_press: root.switchToSignup()
                    
""")

class Login(Screen):
    def switchToSignup(self):
        self.manager.current='signupp'
