from tkinter import *
from math import sqrt

root = Tk()
root.title('Calculator of Opovrongsho') #Don't mind the queer choice of name

memory = [0]
operationmem = '+'


display = Label(root, bg='#B7DCFB', text='', width=30, height=3, font='50')
display.grid(row=0, column=0, columnspan=3)


#Numerical Buttons Defined
button_width, button_height = 12, 3
button1 = Button(root, text='1', width=button_width, height=button_height, pady=5, command=lambda:log(button1['text']))
button2 = Button(root, text='2', width=button_width, height=button_height, pady=5, command=lambda:log(button2['text']))
button3 = Button(root, text='3', width=button_width, height=button_height, pady=5, command=lambda:log(button3['text']))
button4 = Button(root, text='4', width=button_width, height=button_height, pady=5, command=lambda:log(button4['text']))
button5 = Button(root, text='5', width=button_width, height=button_height, pady=5, command=lambda:log(button5['text']))
button6 = Button(root, text='6', width=button_width, height=button_height, pady=5, command=lambda:log(button6['text']))
button7 = Button(root, text='7', width=button_width, height=button_height, pady=5, command=lambda:log(button7['text']))
button8 = Button(root, text='8', width=button_width, height=button_height, pady=5, command=lambda:log(button8['text']))
button9 = Button(root, text='9', width=button_width, height=button_height, pady=5, command=lambda:log(button9['text']))
button0 = Button(root, text='0', width=button_width, height=button_height, pady=5, command=lambda:log(button0['text']))

blist = [button1['text'], button2['text'], button3['text'], button4['text'], button5['text'], button6['text'], button7['text'], button8['text'], button9['text'], button0['text']]

def log(button_num): #Logs Numbers to the Display Label
	display['text'] += blist[int(button_num)-1]

#Operational Functions
def clear():
	display['text'] = ''
	memory[0] = 0

def add():
	global operationmem
	operationmem = '+'
	memory[0] = (display['text'])
	display['text'] = ''

def substract():
	global operationmem
	operationmem = '-'
	memory[0] = (display['text'])
	display['text'] = ''

def multiply():
	global operationmem
	operationmem = '*'
	memory[0] = (display['text'])
	display['text'] = ''

def divide():
	global operationmem
	operationmem = '/'
	memory[0] = (display['text'])
	display['text'] = ''	

def rooot():
	global operationmem
	operationmem = '√'
	memory[0] = (display['text'])
	# display['text'] = str(sqrt(int(memory[0])))
	x = sqrt(int(memory[0]))
	if x == int(x):
		display['text'] = str(int(x))

	else:
		display['text'] = str(x)

def equals():
	if operationmem == '+':
		display['text'] = str(int(float(memory[0])+float(display['text'])))

	elif operationmem == '-':
		display['text'] = str(float(memory[0])-float(display['text']))

	elif operationmem == '*':
		display['text'] = str(float(memory[0])*float(display['text']))

	elif operationmem == '/':
		x = float(memory[0])/float(display['text'])
		if x == int(x):
			display['text'] = str(int(x))

		else:
			display['text'] = str(x)

#Operational Buttons Defined
buttton_add = Button(root, text='+', width=button_width, height=button_height, pady=5, command=add)
button_substract = Button(root, text='-', width=button_width, height=button_height, pady=5, command=substract)
button_multiply = Button(root, text='*', width=button_width, height=button_height, pady=5, command=multiply)
button_divide = Button(root, text='/', width=button_width, height=button_height, pady=5, command=divide)
button_sqrt = Button(root, text='√', width=button_width, height=button_height, pady=5, command=rooot)
button_equal = Button(root, text='=', width = button_width, height=button_height-1, pady=5, command=equals)
clr = Button(root, text='CLR',height=2, width=22, padx=12, pady=5, command=clear).grid(row=6, column=0, columnspan=2)


#Packing the Buttons
button7.grid(row=1, column=0, sticky='w')
button8.grid(row=1, column=1)
button9.grid(row=1, column=2, sticky='e')

button4.grid(row=2, column=0, sticky='w')
button5.grid(row=2, column=1)
button6.grid(row=2, column=2, sticky='e')

button1.grid(row=3, column=0, sticky='w')
button2.grid(row=3, column=1)
button3.grid(row=3, column=2, sticky='e')

button0.grid(row=4, column=1)

buttton_add.grid(row=4, column=2, sticky='e')
button_substract.grid(row=5, column=2, sticky='e')
button_multiply.grid(row=4, column=0, sticky='w')
button_divide.grid(row=5, column=0, sticky='w')
button_sqrt.grid(row=5, column=1)
button_equal.grid(row=6, column=2, sticky='e')





root.mainloop()