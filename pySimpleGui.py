import PySimpleGUI as sg
from rich import print

presidente_X = 0
presidente_y = 0

sg.theme('DarkAmber')

layout = [ 
    [sg.Text("Bem vindo. Digite o número do seu candidato: ")],
    [sg.Text("Digite 001 para o presidente x: ")],
    [sg.Text("Digite 002 para o presidente y: ")],
    [sg.Text("Digite aqui sua opção: "), sg.Input()],
    [sg.Button("Ok"), sg.Button("Cancel")]
]

#  Create the window.
window = sg.Window("Hello world.", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel":
        break
    print("Você digitou a opção: ", values[0])
    if values[0] == "001":
        presidente_X += 1
    else:
        presidente_y += 1
    
    print("**"*30)
    print(f"O presidente X tem [bold][blue]{presidente_X}[/][/] votos ")
    print(f"O presidente y tem [bold][blue]{presidente_y}[/][/] votos ")
    print("**"*30)
    
window.close()
