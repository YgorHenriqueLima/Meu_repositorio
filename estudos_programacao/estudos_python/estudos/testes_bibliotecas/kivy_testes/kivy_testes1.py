from kivy.app import App
from kivy.app import Builder

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


# criação de widgets
class MeuAplicativo(App):
    def build(self):
        # caixa de texto
        box = BoxLayout(orientation='vertical')
        # botão e um texto
        button = Button(text='Botao1', font_size=30)
        # texto para aparecer na janela
        self.label = Label(text='Texto1', font_size=30)
        # inserir o botão e um texto na janela, na caixa
        box.add_widget(button)
        box.add_widget(self.label)
        return box


MeuAplicativo().run()