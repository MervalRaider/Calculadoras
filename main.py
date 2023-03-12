import PySimpleGUI as sg
import datetime as dt


class Calculadora:
    def TNA_TEA(tna, n):
        tna = tna/100
        TEA = ((1 + tna / n) ** n - 1)*100
        return f'TEA: {round(TEA,2)}%'

    def TEA_TNA(tea,n):
        tea = tea / 100
        TNA = (n*((1+tea)**(1/n)-1))*100
        return f'TNA: {round(TNA,2)}%'

    def dias(fecha1, fecha2):
        dia, mes, ano = fecha1.split('/')
        dia2, mes2, ano2 = fecha2.split('/')

        dia1 = dt.date(int(ano), int(mes), int(dia))
        dia2 = dt.date(int(ano2), int(mes2), int(dia2))

        dias = dia2 - dia1

        return f'Días entre fechas: {dias.days}'

    def equivalencia(tasa, partiendo_de='interes' , dias=365):
        tasa = tasa/100
        if partiendo_de == 'interes':
            equiv = tasa/(1+(dias/365)*tasa)
            return f'La tasa de descuento equivalente es: {round(equiv*100,2)}%'
        elif partiendo_de == 'descuento':
            equiv = tasa/(1-(dias/365)*tasa)
            return f'La tasa de interés equivalente es: {round(equiv * 100, 2)}%'
        else:
            return 'No especificó desde qué tasa parte'




sg.theme('DarkBlue1')
layout= [   [sg.Text('Elija operación')]
    ,[sg.Radio('TNA a TEA','g1',key='opcion1'),
    sg.Radio('TEA a TNA','g1',key='opcion2'),
      sg.Radio('Días entre fechas','g1',key='opcion3'),
      sg.Radio('Equivalencia de tasas','g1',key='opcion4')],
            [sg.Button('Ir a la app'), sg.Exit('Cerrar')]]

window = sg.Window('Calculadora',layout)

while True:
    event, values = window.read()
    if values['opcion1'] == True and event=='Ir a la app':
        layout2 = [[sg.Text('TNA:'),sg.InputText()],
                   [sg.Text('Períodos al año:'), sg.InputText()],
                   [sg.Button('Calcular'),sg.Exit('Cerrar')]]
        window2 = sg.Window('TNA A TEA',layout2)
        while True:
            event1, values1 = window2.read()
            if event1 == 'Calcular':
                tasa = Calculadora.TNA_TEA(float(values1[0]),float(values1[1]))
                sg.popup(tasa, image=sg.EMOJI_BASE64_HAPPY_BIG_SMILE)

            if event == sg.WIN_CLOSED or event1 == 'Cerrar':
                window2.close()
                break

    elif values['opcion2'] == True and event=='Ir a la app':
        layout2 = [[sg.Text('TEA:'), sg.InputText()],
                   [sg.Text('Períodos al año:'), sg.InputText()],
                   [sg.Button('Calcular'),sg.Exit('Cerrar')]
                   ]
        window2 = sg.Window('TEA a TNA', layout2)
        while True:
            event1, values1 = window2.read()
            if event1 == 'Calcular':
                tasa = Calculadora.TEA_TNA(float(values1[0]), float(values1[1]))
                sg.popup(tasa, image=sg.EMOJI_BASE64_HAPPY_BIG_SMILE)

            if event == sg.WIN_CLOSED or event1 == 'Cerrar':
                window2.close()
                break

    elif values['opcion3'] == True and event == 'Ir a la app':
        layout2 = [[sg.Text('Fecha Inicial:'), sg.InputText()],
                   [sg.Text('Fecha Final:'), sg.InputText()],
                   [sg.Button('Calcular'), sg.Exit('Cerrar')]
                   ]
        window2 = sg.Window('Calculadora de días', layout2)
        while True:
            event1, values1 = window2.read()
            if event1 == 'Calcular':
                dias = Calculadora.dias(values1[0], values1[1])
                sg.popup(dias, image=sg.EMOJI_BASE64_HAPPY_BIG_SMILE)

            if event == sg.WIN_CLOSED or event1 == 'Cerrar':
                window2.close()
                break

    elif values['opcion4'] == True and event=='Ir a la app':
        layout2 = [[sg.Radio('Busco tasa de interés partiendo de descuento','equivalencia', key='i'),
                    sg.Radio('Busco tasa de descuento partiendo de interés','equivalencia', key='d')],
                [sg.Text('Tasa:'), sg.InputText()],
                   [sg.Text('Días:'), sg.InputText()],
                   [sg.Button('Calcular'), sg.Exit('Cerrar')]
                   ]
        window2 = sg.Window('Equivalencia de tasas', layout2)
        while True:
            event1, values1 = window2.read()
            if event1 == 'Calcular' and values1['d']==True:
                d = Calculadora.equivalencia(tasa=float(values1[0]),partiendo_de='interes',dias=float(values1[1]))
                sg.popup(d, image=sg.EMOJI_BASE64_HAPPY_BIG_SMILE)
            elif event1 == 'Calcular' and values1['i']==True:
                i = Calculadora.equivalencia(tasa=float(values1[0]),partiendo_de='descuento',dias=float(values1[1]))
                sg.popup(i, image=sg.EMOJI_BASE64_HAPPY_BIG_SMILE)
            elif event == sg.WIN_CLOSED or event1 == 'Cerrar':
                window2.close()
                break



    elif event == sg.WIN_CLOSED or event == 'Cerrar':
        window.close()
        break


