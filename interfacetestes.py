from PySimpleGUI import PySimpleGUI as sg


#layout

sg.theme("black")
layout1 = [
         [sg.Text("Usuario"), sg.Input(key='usuario')],
         [sg.Text("Senha"), sg.Input(key='senha', password_char="*")],
         [sg.Checkbox("salvar loguin")],
         [sg.Button('entrar')]
]
layout2 = [
    [sg.Text("FOI")]
]
layout3 = [
    [sg.Text("NAO FOI")]
]


#janela
janela = sg.Window("tela de loguin",layout1)
#ler Eventos
while True:
    eventos,valores = janela.read()

    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'entrar':
        if valores['usuario'] == "joao" and valores['senha'] == "123456":
            print("logado")





