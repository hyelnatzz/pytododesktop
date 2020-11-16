from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from models import Base, Todo
from utils import List, Text, Button, create_layout, create_row



#database initialization
engine = create_engine('sqlite:///todo.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#tasklist
todo_list = session.query(Todo).all()


#setup layout
import PySimpleGUI as sg
layout = create_layout(create_row(Text('TO-DO LIST')),
                       create_row(List(values=[i.title for i in todo_list], size=(
                                 None, 3), key='todolist', enable_events=True)),
                       create_row(Button('Add', key='add'), 
                                  Button('Close', button_color=('red', 'white'), key='close')))

window = sg.Window('task list', layout=layout, size=(200,200))


#main loop
while True:

    event, values = window.read()
    if event in (None, 'close'):
        break
    if event == 'add':
        task = sg.popup_get_text('Title of task', 'New Task')
        new_task = Todo()
        new_task.title = task
        session.add(new_task)
        session.commit()
        print(new_task)
        window['todolist'].update(
            values=[i.title for i in session.query(Todo).all()])
    print(values['todolist'])
    sg.popup_ok(values['todolist'])






