from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class Teste(App):
    # O metodo build inicializa e controi o nosso Apçicativo
    def build(self):
        caixa_1 = BoxLayout(orientation='vertical')
        botao_1 = Button(text='Botão 1', font_size=30, on_release=self.incrementar)
        self.label_1 = Label(text='Texto 1', font_size=30)
        caixa_1.add_widget(botao_1)
        caixa_1.add_widget(self.label_1)

        caixa_2 = BoxLayout()
        botao_2 = Button(text='Botão 2')
        label_2 = Label(text='Texto 2')
        caixa_2.add_widget(botao_2)
        caixa_2.add_widget(label_2)

        caixa_1.add_widget(caixa_2)
        return caixa_1

    def incrementar(self, botao):
        self.label_1.text = 'Texto ' + str(int(self.label_1.text[5:]) + 1)


Teste().run()
