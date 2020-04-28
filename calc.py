from tkinter import *
from math import sqrt
# from tkinter.ttk import *

root = Tk()
root.title('Calculator of Opovrongsho') #Don't mind the queer choice of name
root.geometry('300x500')

#Key Icons Below
delete_icon = PhotoImage(file="C:/Users/Administrator/Desktop/Program Files/Calculator Project/TkinterCalc/deleteKeyIcon.gif")

#Calculation Memory
memory = [0]
operationmem = ''

#Defining and Placing Frames
displayFrame = Frame(root)
displayFrame.place(relwidth=1, relheight=.15, anchor='nw')

buttonFrame = Frame(root, bg='blue')
buttonFrame.place(relx=0, rely=.15, relwidth=1, relheight=.85)


#Defining and Placing the Display of the Calculator
display = Label(displayFrame, bg='#B7DCFB', text='', font=('', 18))
display.place(relwidth=1, relheight=1)


#Numerical Buttons Defined
button_width, button_height = 12, 3
button1 = Button(buttonFrame, text='1', width=button_width, height=button_height, pady=5, command=lambda:log(button1['text']))
button2 = Button(buttonFrame, text='2', width=button_width, height=button_height, pady=5, command=lambda:log(button2['text']))
button3 = Button(buttonFrame, text='3', width=button_width, height=button_height, pady=5, command=lambda:log(button3['text']))
button4 = Button(buttonFrame, text='4', width=button_width, height=button_height, pady=5, command=lambda:log(button4['text']))
button5 = Button(buttonFrame, text='5', width=button_width, height=button_height, pady=5, command=lambda:log(button5['text']))
button6 = Button(buttonFrame, text='6', width=button_width, height=button_height, pady=5, command=lambda:log(button6['text']))
button7 = Button(buttonFrame, text='7', width=button_width, height=button_height, pady=5, command=lambda:log(button7['text']))
button8 = Button(buttonFrame, text='8', width=button_width, height=button_height, pady=5, command=lambda:log(button8['text']))
button9 = Button(buttonFrame, text='9', width=button_width, height=button_height, pady=5, command=lambda:log(button9['text']))
button0 = Button(buttonFrame, text='0', width=button_width, height=button_height, pady=5, command=lambda:log(button0['text']))

blist = [button1['text'], button2['text'], button3['text'], button4['text'], button5['text'], button6['text'], button7['text'], button8['text'], button9['text'], button0['text']]

def log(button_num): #Logs Numbers to the Display Label
	display['text'] += blist[int(button_num)-1]

#Operational Functions
def clear():
	display['text'] = ''
	memory[0] = 0

def delete():
	if len(display['text']) != 0:
		x = list(display['text'])
		x.remove(x[-1])
		display['text'] = ''.join(x)
		

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
	x = sqrt(float(memory[0]))
	if x == int(x):
		display['text'] = str(int(x))

	else:
		display['text'] = str(x)

def point():
	display['text'] += '.'

def equals():
	if operationmem == '+':
		x = float(memory[0])+float(display['text'])
		if x == int(x):
			display['text'] = str(int(x))

		else:
			display['text'] = str(x)

	elif operationmem == '-':
		x = float(memory[0])-float(display['text'])
		if x == int(x):
			display['text'] = str(int(x))

		else:
			display['text'] = str(x)

	elif operationmem == '*':
		x = float(memory[0])*float(display['text'])
		if x == int(x):
			display['text'] = str(int(x))

		else:
			display['text'] = str(x)

	elif operationmem == '/':
		x = float(memory[0])/float(display['text'])
		if x == int(x):
			display['text'] = str(int(x))

		else:
			display['text'] = str(x)

#Operational Buttons Defined
buttton_add = Button(buttonFrame, text='+', width=button_width, height=button_height, pady=5, command=add)
button_substract = Button(buttonFrame, text='_', width=button_width, height=button_height, pady=5, command=substract)
button_multiply = Button(buttonFrame, text='*', width=button_width, height=button_height, pady=5, command=multiply)
button_divide = Button(buttonFrame, text='/', width=button_width, height=button_height, pady=5, command=divide)
button_sqrt = Button(buttonFrame, text='√', width=button_width, height=button_height, pady=5, command=rooot)
button_equal = Button(buttonFrame, text='=', padx=133.5, height=button_height, pady=5, command=equals)
clr = Button(buttonFrame, text='CLR',height=button_height, width=button_width, pady=5, command=clear)
button_decimal = Button(buttonFrame, text='.', width=button_width, height=button_height, pady=5, command=point)
delete_button = Button(buttonFrame, image=delete_icon, width=88, height=58, command=delete)

#Placing the Buttons


root.mainloop()