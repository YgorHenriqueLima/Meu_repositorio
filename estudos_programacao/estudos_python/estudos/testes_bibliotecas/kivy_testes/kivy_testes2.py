from kivy.app import App
from kivy.app import Builder
from kivy.uix.boxlayout import BoxLayout



class Incrementar(BoxLayout):
    pass

class MeuAplicativo(App):
    def build(self):
        return Incrementar()


MeuAplicativo().run()
