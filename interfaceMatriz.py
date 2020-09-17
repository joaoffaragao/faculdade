from PySimpleGUI import PySimpleGUI as sg
import numpy as np  # Importa módulo numpy para criação das matrizes e vetores
from scipy import linalg  # Importa linalg de scipy para solução sistemas de equações lineares
tipo_matriz =1

if tipo_matriz == 1:
    #layout
    sg.theme('black')
    layout= [
        [sg.Text("",size=(5,0)),sg.Text("1",size=(5,0)),sg.Text("2",size=(5,0)),sg.Text("3",size=(5,0)),sg.Text("4",size=(5,0)),sg.Text("",size=(5,0)),sg.Text("1",size=(5,0))],
        [sg.Text("",size=(5,0)),sg.Input(key="Aij11",size=(5,0)),sg.Input(key="Aij12",size=(5,0)),sg.Input(key="Aij13",size=(5,0)),sg.Input(key="Aij14",size=(5,0)),sg.Text("",size=(5,0)),sg.Input(key="Bij11",size=(5,0))],
        [sg.Text("[A]=",size=(5,0)),sg.Input(key="Aij21",size=(5,0)),sg.Input(key="Aij22",size=(5,0)),sg.Input(key="Aij23",size=(5,0)),sg.Input(key="Aij24",size=(5,0)),sg.Text("[B]=",size=(5,0)),sg.Input(key="Bij21",size=(5,0))],
        [sg.Text("", size=(5, 0)), sg.Input(key="Aij31", size=(5, 0)), sg.Input(key="Aij32", size=(5, 0)),sg.Input(key="Aij33",size=(5,0)),sg.Input(key="Aij34",size=(5,0)),sg.Text("",size=(5,0)),sg.Input(key="Bij31",size=(5,0))],
        [sg.Text("", size=(5, 0)), sg.Input(key="Aij41", size=(5, 0)), sg.Input(key="Aij42", size=(5, 0)),sg.Input(key="Aij43",size=(5,0)),sg.Input(key="Aij44",size=(5,0)),sg.Text("",size=(5,0)),sg.Input(key="Bij41",size=(5,0))],
        [sg.Button("entrar")]
    ]
    #janela
    janela = sg.Window("calculo Matriz",layout)
    #eventos
    eventos, valores = janela.read()

    entrada = True
    while entrada:
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == "entrar":

            # Cria a matriz A
            A =[float(valores["Aij11"]), float(valores["Aij12"]), float(valores["Aij13"]), float(valores["Aij14"])],\
               [float(valores["Aij21"]), float(valores["Aij22"]), float(valores["Aij23"]), float(valores["Aij24"])],\
               [float(valores["Aij31"]), float(valores["Aij32"]), float(valores["Aij33"]), float(valores["Aij34"])],\
               [float(valores["Aij41"]), float(valores["Aij42"]), float(valores["Aij43"]), float(valores["Aij41"])]

            b = ([[float(valores["Bij11"])], [float(valores["Bij21"])], [float(valores["Bij31"])], [float(valores["Aij41"])]])


            print("matriz A", A)


            print("matriz B", b)


            x = linalg.solve(A, b)  # Resolve o sistema utilizando linalg.solve
            print('x = ', x)
            entrada=False
elif tipo_matriz ==2:
    # layout
    sg.theme('black')
    layout = [
        [sg.Text("", size=(5, 0)), sg.Text("1", size=(5, 0)), sg.Text("2", size=(5, 0)), sg.Text("3", size=(5, 0)),sg.Text("4", size=(5, 0)), sg.Text("1", size=(5, 0))],
        [sg.Text("", size=(5, 0)), sg.Input(key="Aij11", size=(5, 0)), sg.Input(key="Aij12", size=(5, 0)),sg.Input(key="Aij13", size=(5, 0)), sg.Text("", size=(5, 0)),sg.Input(key="Bij11", size=(5, 0))],
        [sg.Text("[A]=", size=(5, 0)), sg.Input(key="Aij21", size=(5, 0)), sg.Input(key="Aij22", size=(5, 0)),sg.Input(key="Aij23", size=(5, 0)), sg.Text("[B]=", size=(5, 0)), sg.Input(key="Bij21", size=(5, 0))],
        [sg.Text("", size=(5, 0)), sg.Input(key="Aij31", size=(5, 0)), sg.Input(key="Aij32", size=(5, 0)),sg.Input(key="Aij33", size=(5, 0)), sg.Text("", size=(5, 0)),sg.Input(key="Bij31", size=(5, 0))],
        [sg.Button("entrar")]
    ]
    # janela
    janela = sg.Window("calculo Matriz", layout)
    # eventos
    eventos, valores = janela.read()

    entrada = True
    while entrada:
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == "entrar":
            # Cria a matriz A
            A = [float(valores["Aij11"]), float(valores["Aij12"]), float(valores["Aij13"])],\
                [float(valores["Aij21"]), float(valores["Aij22"]), float(valores["Aij23"])],\
                [float(valores["Aij31"]), float(valores["Aij32"]), float(valores["Aij33"]),]

            b = ([[float(valores["Bij11"])], [float(valores["Bij21"])], [float(valores["Bij31"])]])

            print("matriz A", A)

            print("matriz B", b)

            x = linalg.solve(A, b)  # Resolve o sistema utilizando linalg.solve
            print('x = ', x)
            entrada = False