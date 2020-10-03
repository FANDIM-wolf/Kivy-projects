
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout



import sqlite3
#window can not change size 
#Config.set('graphics' , 'resizable' ,'0');

#size of the window
Config.set('graphics' , 'width' ,'450');
Config.set('graphics' , 'height' ,'640');

#padding: right , up , left , down
#spacing: it is space bettwen widgets 

class Main(App):
	def build(self):
		bl = BoxLayout(orientation='horizontal' , padding=[0,0,0,100] ,spacing=100)

		bl.add_widget(Button(text="Button1" , font_size="15"))
		bl.add_widget(Button(text="Button2" , font_size="15"))
		bl.add_widget(Button(text="Button3" , font_size="15"))
		bl.add_widget(Button(text="Button4" , font_size="15"))

		return bl



		




if __name__ == '__main__':
    Main().run()