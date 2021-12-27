from datetime import datetime
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from models import Base, Todo
from utils import List, Text, Button, create_layout, create_row, Table, sg




#database initialization
engine = create_engine('sqlite:///todo.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#add to db
def add_to_db(title, description):
    """ Adds task to the database """
    new_task = Todo()
    new_task.title = title
    new_task.description = description
    new_task.date_created = datetime.now().strftime('%d/%m/%Y')
    session.add(new_task)
    session.commit()


#tasklist
todo_list = session.query(Todo).filter_by(date_created= datetime.now().strftime('%d/%m/%Y')).all()

print(len(todo_list))

no_task = Text('You have not added a task today', key = 'no task', font=('arial', 20), visible=False)


#get and format current time
def get_time():
    now = datetime.now()
    return now.strftime("%I:%M%p %a %d. %b %Y")

#creating table

table = Table(values=[[i+1, todo_list[i].title] for i in range(len(todo_list))],
                headings=['s/no', 'Title'], size=(None, 10),
                col_widths=[10, 100], max_col_width=100, key='todolist',
                enable_events=True, justification='left',
                alternating_row_color=('red'), row_height=30,
                header_background_color='black', header_text_color='white',
                font=('arial', 12), visible=False)
values = []
if len(todo_list) < 1:
    print(len(values))
    values = [['-', "You haven't created any task today!"]]
else:
    values = [[i+1, todo_list[i].title] for i in range(len(todo_list))]

#setup layout
layout = create_layout(create_row(Text('TO-DO LIST'), Button('Add New Task', key='add_new', border_width=5, button_color=('white', 'blue')),Text('', size=(20, None)), Text(get_time())),
                       create_row(Text('*click on any for more info and editing option', font=('arial', 8), text_color='yellow')),
                       create_row(Table(values=values,
                                        headings=['s/no', 'Title'], size=(None, 10),
                                        col_widths=[10, 100], max_col_width=100, key='todolist',
                                        enable_events=True, justification='left',
                                        alternating_row_color=('red'), row_height=30,
                                        header_background_color='black', header_text_color='white',
                                        font=('arial', 12), visible=True)),
                       create_row(Button('Add New Task', key='add',  border_width=5, button_color=('white', 'blue')),
                                  Text('', size=(40, None)),
                                  Button('Close', button_color=('white', 'red'), key='close', border_width=5)))

window = sg.Window('myTask', layout=layout, size=(550,430))


#main loop
while True:
    """if len(todo_list) < 1:
        print('empty list')
        window['no task'].update(visible=True)
        window['todolist'].update(visible=False)"""
    event, values = window.read()
    if event in (None, 'close'):
        break

    #adding task
    if event in ['add', 'add_new']:
        title = sg.popup_get_text('Title of task', 'New Task')
        description = sg.popup_get_text(f'Description for "{title}"', 'Task Description', default_text='description')
        if title != None:
            add_to_db(title, description)

        #get updated list
        todo_list = session.query(Todo).all()
        if len(todo_list) > 0:
            window['todolist'].update(
                values=[[i+1, todo_list[i].title] for i in range(len(todo_list))])

    if 'todolist' in values.keys():
         print(values['todolist'])

    #show details
    if event == 'todolist':
        task_info = todo_list[values['todolist'][0]]
        sg.popup_ok('Title: '+task_info.title + '\n________________________\n' +
                    'Description\n' + task_info.description, title='Task Detail')
        
        






