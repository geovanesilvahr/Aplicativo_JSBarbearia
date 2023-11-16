#coding: utf-8

################################################
##########   Author: Geovane Silva   ###########
########    Project: My Project   #########
#############    Version: 0.0.1   ##############
################################################

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.lang import Builder

#usuarios = {}

class TelaCadastroWindow(FloatLayout):

    def __init__(self, **wargs):
        super(TelaCadastroWindow, self).__init__(**wargs)

#      Tentatita falha de iniciar a tela com um Popup para conter informações para o Usuário
   
#        box = BoxLayout(orientation = 'vertical')
#        lb = Label(text="Você deverá mostr", font_size = 14)
#        pop = Popup(title="Você possui 1 corte GRATIS!", content=box)
#        box.add_widget(lb)
#        pop.open()

    def cadastrar(self):
        pass

    def voltar(self):
        self.parent.parent.current = 'scrn_login'

Builder.load_file('cadastro/telacadastro.kv')

class TelaCadastroApp(App):

    def build(self):
        return TelaCadastroWindow()

if __name__ == '__main__':
    TelaCadastroApp().run()
