from tkinter import *
import tkinter.font as font

query = str()
container = str()
result = str()

root = Tk()
root.geometry('336x350')
root.resizable(0,0)
root.config(bg='white')

def number_creator(num):
	query += num

def addition():
	pass

def subtraction():
	pass

def multiplication():
	pass

def division():
	pass

def calculate_result():
	pass


class NumberButton(Button):

	button_font = font.Font(family='helvetica', size=25)

	def __init__(self, master, text, command, *args, **kwargs):
		Button.__init__(self, master, *args, **kwargs)
		self.master = master
		self['height'] = 1
		self['width'] = 4
		self['text'] = text
		self['bg'] = '#f2f2f2'
		self['bd'] = 1
		self['font'] = NumberButton.button_font
		self['fg'] = '#404040'
		self['command'] = command


class OperationButton(Button):

	button_font = font.Font(family='helvetica', size=25)

	def __init__(self, master, text, command, *args, **kwargs):
		Button.__init__(self, master, *args, **kwargs)
		self.master = master
		self['height'] = 1
		self['width'] = 4
		self['text'] = text
		self['bg'] = '#d9d9d9'
		self['bd'] = 1
		self['font'] = NumberButton.button_font
		self['fg'] = '#404040'
		self['command'] = command



placeholder = OperationButton(root, 'a', 'a')
placeholder.grid(row=5, column=0)

b0 = NumberButton(root, 0, '0')
b0.grid(row=5, column=1)

bdot = OperationButton(root, '.', '.')
bdot.grid(row=5, column=2)

bresult = OperationButton(root, '=', calculate_result)
bresult.grid(row=5, column=3)


b1 = NumberButton(root, 1, '1')
b1.grid(row=4, column=0)

b2 = NumberButton(root, 2, '2')
b2.grid(row=4, column=1)

b3 = NumberButton(root, 3, '3')
b3.grid(row=4, column=2)

baddition = OperationButton(root, '+', addition)
baddition.grid(row=4, column=3)


b4 = NumberButton(root, 4, '4')
b4.grid(row=3, column=0)

b5 = NumberButton(root, 5, '5')
b5.grid(row=3, column=1)

b6 = NumberButton(root, 6, '6')
b6.grid(row=3, column=2)

bsubtraction = OperationButton(root, '-', subtraction)
bsubtraction.grid(row=3, column=3)


b7 = NumberButton(root, 7, '7')
b7.grid(row=2, column=0)

b8 = NumberButton(root, 8, '8')
b8.grid(row=2, column=1)

b9 = NumberButton(root, 9, '9')
b9.grid(row=2, column=2)

bmultiplication = OperationButton(root, 'x', multiplication)
bmultiplication.grid(row=2, column=3)


bclear = OperationButton(root, 'C', 'R')
bclear.config(width=6)
bclear.grid(row=1, columnspan=3, sticky=W)

bremove = OperationButton(root, 'R', 'R')
bremove.config(width=6)
bremove.grid(row=1, columnspan=3, sticky=E)

bdivision = OperationButton(root, '/', division)
bdivision.grid(row=1, column=3)




root.mainloop()