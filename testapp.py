


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout



import sqlite3
#window can not change size 
#Config.set('graphics' , 'resizable' ,'0');

#size of the window
Config.set('graphics' , 'width' ,'450');
Config.set('graphics' , 'height' ,'640');

class TestApp(App):
    
    def build(self):
        

        fl = FloatLayout(size=(300,300))
        
        fl.add_widget(Button (text='hello world' ,font_size=14 ,on_press=self.btn_press,
        	background_color=[1,0,0,1] ,
        	background_normal='',
        	size_hint=(.5,.25),
        	pos=(0,20)))
        return fl

    def btn_press(self,instance):
    	print("Button is pressed")
    	instance.text = "Button is pressed"





if __name__ == '__main__':
    TestApp().run()



