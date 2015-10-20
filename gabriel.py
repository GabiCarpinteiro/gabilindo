from tkinter import *
app = tk()
app.title ("teste de janela")
app.geometry ('300x100+100.200')
quant_botao01 = IntVar()
quant_botao01.set(0)
quant_botao02 = IntVar ()
quant_botao02.set (0)
def apertou01 ():
    quant_botao01.set(quant_botao01.get() + 1)
    def apertou02 ():
        quant_botao02.set(quant_botao02.get() + 1)
        lab = Label(app,text='Aperte os botoes')
        lab.pack()

