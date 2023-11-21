from kivy.clock import Clock
from kivy.graphics.vertex_instructions import Ellipse, Line, Rectangle
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

Builder.load_file("canvas_exemples.kv")

class CanvasExemple1(Widget):
    pass

class CanvasExemple2(Widget):
    pass

class CanvasExemple3(Widget):
    pass

class CanvasExemple4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(0,0, 100,100), width=2)
            Line(ellipse=(300,30,100,200),width=4)
            Line(circle=(100,200,50),width=2)
            #Line(rectangle=(200,400,100,150),width=3)
            self.rect = Rectangle(pos=(500,200), size=(100,50))
            
    def on_click_to_move(self):
        x,y = self.rect.pos
        w,h = self.rect.size
        if x+w < self.width:
            x += 10
            self.rect.pos = x,y

class CanvasExemple5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size= 50
        self.vx = 3
        self.vy = 5
        with self.canvas:
            self.ball = Ellipse(pos=self.center, size=(self.ball_size,self.ball_size))
            # Le module Clock permet de planifier des fonctions à être appelées à intervalles réguliers.
            Clock.schedule_interval(self.update,1/60)
    
    # La méthode on_size dans Kivy est appelée automatiquement lorsqu'il y a un changement de taille du widget.Cependant, vous devez déclarer la méthode avec trois paramètres, même si vous n'avez pas besoin de les utiliser explicitement.
    def on_size(self, instance, value):
        self.ball.pos= (self.center_x-self.ball_size/2, self.center_y-self.ball_size/2)
        
    def update(self,dt):
        x,y = self.ball.pos
        w,h = self.ball.size
        """ Mon code pour l'exercice
        if y+h == self.height:
            self.vy = -self.vy
        if x+w == self.width:
            self.vx = -self.vx
        if y+h == 0:
            self.vy = -self.vy
        if x+w == 0:
            self.vx = -self.vx """
        
        if y+self.ball_size > self.height:
            y = self.height-self.ball_size
            self.vy = -self.vy
        if x+self.ball_size > self.width:
            x = self.width - self.ball_size
            self.vx = -self.vx
        if y < 0:
            y = 0
            self.vy = -self.vy
        if x < 0:
            x = 0
            self.vx = -self.vx
        x += self.vx
        y += self.vy
        self.ball.pos =(x,y)
        
class CanvasExemple6(Widget):
    pass

class CanvasExemple7(BoxLayout):
    pass