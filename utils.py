import PySimpleGUI as sg

class MakeWindow(sg.Window):
    pass

class Text(sg.Text):
    pass

class Button(sg.Button):
    pass

class List(sg.Listbox):
    pass


def create_row(*args):
    return [i for i in args]

def create_layout(*args):
    return [i for i in args]

"""
layout = make_layout(make_row(Text('first test'), Button('second test')), 
                     make_row(Text('first test'), Button('second test')))

window = MakeWindow('Tester', layout=layout)
event, values = window.read()

print(make_layout(make_row(1, 2), make_row(1, 2)))"""

