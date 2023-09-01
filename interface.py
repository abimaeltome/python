import tkinter
from tkinter import Button
from tkinter import Entry
from tkinter import Label
from tkinter import messagebox

def acao():
    print("Botão pressionado!")
    msg = messagebox.showinfo("Alerta!", texto.get())

principal = tkinter.Tk()
#código da iterface aqui
botao = Button(principal, text="Olá", command=acao)
botao.grid(row=0, column=2)

texto = Entry(principal)
texto.grid(row=0, column=1)

etiqueta = Label(principal, text="Label")
etiqueta.grid(row=0, column=0)


principal.mainloop()

