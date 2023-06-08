import PySimpleGUI as sg

layout = [
    [sg.Text("Pegar Cotação da Moeda")],
    [sg.InputText(key="nome_cotacao")],
    [sg.Button("Pegar Cotação"), sg.Button("Cancelar")],
    [sg.Text("", key="texto_cotacao")],
]

janela = sg.Window("Sistema de Cotações", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break

janela.close()