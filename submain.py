from utils import *

row1 = create_row(Text('first trial', key='t1'), Button('first button', key='b1'))

layout = create_layout(row1)

window = MakeWindow('success', layout=layout)
event, values = window.read()

print(values)
