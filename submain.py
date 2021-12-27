import PySimpleGUI as sg

name = ['hye', 'nat']
layout = [[sg.Table(values=[['write', i+1, 'dddd'] for i in range(6)], headings=['numbers','num1', 'rand'], key='table', display_row_numbers=True)]]


window = sg.Window('Table', layout=layout)

event, values = window.read()

if event == 'table':
    sg.popup_ok(name[values['table'][0]])