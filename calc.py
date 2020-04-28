from tkinter import *
from math import sqrt
# from tkinter.ttk import *

root = Tk()

#Icons Below
delete_icon = PhotoImage(file="C:/Users/Administrator/Desktop/Program Files/Calculator Project/TkinterCalc/deleteKeyIcon.gif")
main_icon = PhotoImage(file="C:/Users/Administrator/Desktop/Program Files/Calculator Project/TkinterCalc/main_icon.png")

root.title('Calculator of Opovrongsho') #Don't mind the queer choice of name
root.geometry('350x600')
root.iconphoto(False, main_icon)

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
button_width, button_height = 1/3, 1/7
button1 = Button(buttonFrame, text='1', pady=5, command=lambda:log(button1['text']))
button2 = Button(buttonFrame, text='2', pady=5, command=lambda:log(button2['text']))
button3 = Button(buttonFrame, text='3', pady=5, command=lambda:log(button3['text']))
button4 = Button(buttonFrame, text='4', pady=5, command=lambda:log(button4['text']))
button5 = Button(buttonFrame, text='5', pady=5, command=lambda:log(button5['text']))
button6 = Button(buttonFrame, text='6', pady=5, command=lambda:log(button6['text']))
button7 = Button(buttonFrame, text='7', pady=5, command=lambda:log(button7['text']))
button8 = Button(buttonFrame, text='8', pady=5, command=lambda:log(button8['text']))
button9 = Button(buttonFrame, text='9', pady=5, command=lambda:log(button9['text']))
button0 = Button(buttonFrame, text='0', pady=5, command=lambda:log(button0['text']))

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
buttton_add = Button(buttonFrame, text='+', pady=5, command=add)
button_substract = Button(buttonFrame, text='_', pady=5, command=substract)
button_multiply = Button(buttonFrame, text='*', pady=5, command=multiply)
button_divide = Button(buttonFrame, text='/', pady=5, command=divide)
button_sqrt = Button(buttonFrame, text='√', pady=5, command=rooot)
button_equal = Button(buttonFrame, text='=', padx=133.5,  pady=5, command=equals)
button_clr = Button(buttonFrame, text='CLR', pady=5, command=clear)
button_decimal = Button(buttonFrame, text='.', pady=5, command=point)
delete_button = Button(buttonFrame, image=delete_icon, command=delete)

#Placing the Buttons
button7.place(relx=0, rely=0, relheight=button_height, relwidth=button_width)
button8.place(relx=1/3, rely=0, relheight=button_height, relwidth=button_width)
button9.place(relx=2/3, rely=0, relheight=button_height, relwidth=button_width)

button4.place(relx=0, rely=1/7, relheight=button_height, relwidth=button_width)
button5.place(relx=1/3, rely=1/7, relheight=button_height, relwidth=button_width)
button6.place(relx=2/3, rely=1/7, relheight=button_height, relwidth=button_width)

button1.place(relx=0, rely=2/7, relheight=button_height, relwidth=button_width)
button2.place(relx=1/3, rely=2/7, relheight=button_height, relwidth=button_width)
button3.place(relx=2/3, rely=2/7, relheight=button_height, relwidth=button_width)

button0.place(relx=1/3, rely=3/7, relwidth=button_width, relheight=button_height)

button_multiply.place(relx=0, rely=3/7, relwidth=button_width, relheight=button_height)
buttton_add.place(relx=2/3, rely=3/7, relwidth=button_width, relheight=button_height)

button_divide.place(relx=0, rely=4/7, relwidth=button_width, relheight=button_height)
button_sqrt.place(relx=1/3, rely=4/7, relwidth=button_width, relheight=button_height)
button_substract.place(relx=2/3, rely=4/7, relwidth=button_width, relheight=button_height)

button_clr.place(relx=0, rely=5/7, relwidth=button_width, relheight=button_height)
button_decimal.place(relx=1/3, rely=5/7, relwidth=button_width, relheight=button_height)
delete_button.place(relx=2/3, rely=5/7, relwidth=button_width, relheight=button_height)

button_equal.place(relx=0, rely=6/7, relwidth=button_width*3, relheight=button_height)

root.mainloop()