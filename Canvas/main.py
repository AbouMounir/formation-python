from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout

from canvas_exemples import *
from navigation_screen_manager import NavigationScreenManager

""" from kivy.uix.button import Button """
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.widget import Widget


class MyScreenManager(NavigationScreenManager):
    pass

class LeLabApp(App):
    manager = ObjectProperty(None)
    
    def build(self):
        self.manager = MyScreenManager()
        return self.manager
        

LeLabApp().run()