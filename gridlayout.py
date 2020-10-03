from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout



import sqlite3
#window can not change size 
#Config.set('graphics' , 'resizable' ,'0');

#size of the window
Config.set('graphics' , 'width' ,'450');
Config.set('graphics' , 'height' ,'640');

#cols - columns 

class Main(App):
	def build(self):
		bl= GridLayout(cols=4 ,rows=1,padding=[0,0,0,450])
		bl.add_widget(Button(text="Button",font_size="15"))
		bl.add_widget(Button(text="Button",font_size="15"))
		bl.add_widget(Button(text="Button",font_size="15"))
		bl.add_widget(Button(text="Button",font_size="15"))

        #bl.add_widget(Button(text="Button1" , font_size="15"))
		
		return bl



		




if __name__ == '__main__':
    Main().run()