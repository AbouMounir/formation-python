from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.properties import (BooleanProperty, NumericProperty, ObjectProperty,
                             StringProperty)
from kivy.uix.behaviors import CoverBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget

from http_client import HttpClient
from model import Pizza


class PizzaWidget(BoxLayout):
    nom = StringProperty()
    # NumericProperty / BooleanProperty
    ingredients = StringProperty()
    prix = NumericProperty()
    vegetarienne = BooleanProperty()

class MainWidget(FloatLayout):
    recycleview = ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        """ self.pizzas = [
                Pizza("4 fromages", "chèvre, emmental, brie, comté", 9.5, True),
                Pizza("Chorizo", "tomates, chorizo, parmesan", 11.2, False),
                Pizza("Calzone", "fromage, jambon, champignons", 10, False)
            ] """
            
    """  def on_parent(self,widget,parent):
        self.recycleview.data = [pizza.get_dictionary() for pizza in self.pizzas]
        """
        
    HttpClient().get_pizzas()
        
        
class PizzaApp(App):
    pass


PizzaApp().run()