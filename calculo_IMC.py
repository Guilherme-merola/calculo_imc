import PySimpleGUI as sg


def Janela_inicial():
    """Função que define o estilo e layout da interface"""
    estilo = [
        [sg.Text('Peso:', size=5), sg.Input(key='peso', size=10), sg.Text("kilos")],
        [sg.Text('Altura:', size=5), sg.Input(key='altura', size=10), sg.Text("metros", size=6)],
        [sg.Button('Calcular', size=22)],
        [sg.Text('', key='texto')]
    ]

    return sg.Window('Inicio', layout=estilo, finalize=True)


janela1 = Janela_inicial()


while True:
    """Looping responsavel por deixar a janela rodando e pegar os valores dados pelo usuarios para realizar o calculo de IMC"""
    window, event, value = sg.read_all_windows()

    if window == janela1 and event == sg.WIN_CLOSED:
        break
    else:
        peso = value['peso'].replace(',', '.')
        altura = value['altura'].replace(',', '.')
        if len(peso) == 0 and len(altura) == 0:
            janela1['texto'].Update('Informe seus dados')
        else:
            try:
                janela1['texto'].Update(f'Seu IMC é: {round(float(peso) / (float(altura) ** 2), 1)}')
            except:
                janela1['texto'].Update('Digite seus dados corretamente')
        