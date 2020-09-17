from PySimpleGUI import PySimpleGUI as sg


#layout

sg.theme("black")
layout = [
         [sg.Text("Usuario"), sg.Input('usuario')],
         [sg.Text("Senha"), sg.Input('senha',password_char="*")],
         [sg.Checkbox("salvar loguin")],
         [sg.Button('entrar')]
]

#janela
janela = sg.Window("tela de loguin",layout)
#ler Eventos
while True:
    eventos,valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'entrar':
        print("entrou")
        if valores['usuario'] == "joao" and valores['senha'] == "123456":
            print("logado")



