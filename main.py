#Coding: utf-8

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from login.login import LoginWindow
from tela.telawin import TelaWindow

class MainWindow(BoxLayout):

    tela_win = TelaWindow()
    login_win = LoginWindow()

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

        self.ids.scrn_login.add_widget(self.login_win)
        self.ids.scrn_tela.add_widget(self.tela_win)


class MainApp(App):
    def build(self):
        return MainWindow()

if __name__ == '__main__': 
    MainApp().run()
