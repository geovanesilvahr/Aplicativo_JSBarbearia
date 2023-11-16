#Coding: utf-8

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder


#Tela de Login - Primeira Screen executada pelo ScreenManager
class LoginWindow(FloatLayout):

    def __init__(self, **kwargs):
        super(LoginWindow, self).__init__(**kwargs)

    def validar(self, **kwargs):

        self.email = self.ids.txEmail.text
        self.senha = self.ids.txSenha.text

        if self.email == 'admin' and self.senha == 'admin':
            self.parent.parent.current = 'scrn_tela'
            self.ids.sts.text = ''

        else:
            self.ids.sts.color = (1, 0, 0, 1)
            self.ids.sts.text = 'Usuário e/ou Senha Inválida!'
    
    def telaCadastro(self):
        self.parent.parent.current = 'scrn_telacadastro'

Builder.load_file('login/login.kv')

class LoginApp(App):

    def build(self):
        return LoginWindow()



if __name__ == '__main__': 
    LoginApp().run()
