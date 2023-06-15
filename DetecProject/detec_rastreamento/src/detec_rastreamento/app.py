"""
app para rastrear aparelhos eletronicos roubados ou perdidos
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class detec(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction= COLUMN))
        main_box.add(
            toga.Label('cadastre-se'),
            toga.TextInput(placeholder='Email...'),
            toga.PasswordInput(placeholder='senha...'),
            toga.Label('idade'),
            toga.NumberInput(),
            toga.Button('enviar', on_press=self.enviar)
            

        )

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def enviar():
        pass


def main():
    return detec()
