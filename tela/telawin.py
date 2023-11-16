#Coding: utf-8

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class TelaWindow(BoxLayout):

    def __init__(self, **kwargs):
        super(TelaWindow, self).__init__(**kwargs)

    def validar(self, **kwargs):
        self.parent.parent.current = 'scrn_login'

Builder.load_file('tela/telawin.kv')

class TelaWinApp(App):

    def build(self):
        return TelaWindow()

if __name__ == '__main__': 
    TelaWinApp().run()
