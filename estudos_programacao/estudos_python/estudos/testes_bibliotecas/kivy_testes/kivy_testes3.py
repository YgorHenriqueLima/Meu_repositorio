from kivy.app import App
from kivy.app import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
# criando layouts dinâmicos 
class Tarefas(BoxLayout):
    def __init__(self, tarefas,**kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.add_widget(Label(text=tarefa, font_size=30))

class MeuAplicativo(App):
    def build(self):
        return Tarefas(['tomar banho','lavar os pratos','correr'], orientation='horizontal')


MeuAplicativo().run()
