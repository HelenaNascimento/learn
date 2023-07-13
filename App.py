# Importar o App, Builder (GUI - Tela)
# Criar o Aplicativo
# Criar a Função build

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


GUI = Builder.load_file("HelpTI.kv")

Window.size = (300,380)

class HelpTI(App):
    def build(self):
        return GUI



HelpTI().run()
