from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
import math


class CalculadoraJanela(BoxLayout):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        #  Lista de caracteres (texto dos botoes)
        grid_numeros = [7, 8, 9, 4, 5, 6, 1, 2, 3, ".", 0, "%"]
        grid_simbolos = ['(', ')', 'π', '-', '+', '√', 'x', '÷', 'x²', 'C', 'AC', ' mod ']

        # self.numeros = self.ids.numeros - basicamente estou dizendo que a variavel
        # numeros se recebe a id numeros da gridlayoult do arquivo kv. E assim funciona com os ids
        self.numeros = self.ids.numeros
        self.simbolos = self.ids.simbolos

        #  Criação dos botões a partir da lista de caracteres grid_numeros
        for num in grid_numeros:
            botao = Button(text=str(num), background_normal='', background_color=(0.047, 0.553, 0.588, 1.0))
            botao.bind(on_release=self.mostra_conta)
            self.numeros.add_widget(botao)

        #  Criação dos botões a partir da lista de caracteres grid_simbolos
        for simbolo in grid_simbolos:
            botao = Button(text=str(simbolo), background_normal='', background_color=(0.937, 0.643, 0.404, 1.0))
            botao.bind(on_release=self.mostra_conta)
            self.simbolos.add_widget(botao)

        #  Criando um botão para o sinal de igual
        igual = Button(text="=", background_color=(0.992, 0.275, 0.592, 1.0), background_normal='', font_size=26,
                       size_hint_x=0.74)
        igual.bind(on_release=self.expressao)
        self.ids.status_bar.add_widget(igual)

        mensagem = Label(text='Entre em contato pelo e-mail:\nrenan.silva.soares.br@gmail.com')
        mensagem.halign = 'center'
        self.ids.status_bar.add_widget(mensagem)

        logo = Image(source='/home/renan/Downloads/op.jpg', size=self.size)
        self.ids.centro.add_widget(logo)


    # Metodo para mostrar os valores na barra
    def mostra_conta(self, instance):
        informacao = self.ids.informacao

        #
        if instance.text == 'AC':
            informacao.text = ''

        elif instance.text == 'C':
            informacao.text = informacao.text[:-1]

        else:
            informacao.text += instance.text

    def expressao(self, text):
        informacao = self.ids.informacao
        exp = informacao.text
        exp = self.troca_simbolo(exp)
        res = eval(exp)
        informacao.text = str(res)

        self.ids.conta.text = exp
        self.ids.igual.text = '='
        self.ids.resultado.text = str(res)

    def troca_simbolo(self, text):
        troca = text.replace('π', str(math.pi)).replace('x²', '** 2').replace('√', '** 0.5').replace('%', '/100')\
            .replace('x', '*').replace('÷', '/').replace(' mod ', '%')
        return troca


class MyCalculadora(App):
    # O metodo build inicializa e controi o nosso Apçicativo
    def build(self):
        return CalculadoraJanela()


if __name__ == "__main__":
    MyCalculadora().run()
