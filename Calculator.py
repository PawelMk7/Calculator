from tkinter import *
import tkinter.font as font

query = str()
container = str()
result = str()

root = Tk()
root.geometry('300x400')

def number_creator(num):
	query += num

def addition():
	


class NumberButton(Button):

	button_font = font.Font(family='helvetica', size=25)

	def __init__(self, master, text, command, *args, **kwargs):
		Button.__init__(self, master, *args, **kwargs)
		self.master = master
		self['height'] = 1
		self['width'] = 3
		self['text'] = text
		self['bg'] = '#f0ebeb'
		self['bd'] = 1
		self['font'] = NumberButton.button_font
		self['command'] = command



b1 = NumberButton(root, 1, '1')
b1.grid(row=2, column=0)

b2 = NumberButton(root, 2, '2')
b2.grid(row=2, column=1)

b3 = NumberButton(root, 3, '3')
b3.grid(row=2, column=2)

b4 = NumberButton(root, 4, '4')
b4.grid(row=1, column=0)

b5 = NumberButton(root, 5, '5')
b5.grid(row=1, column=1)

b6 = NumberButton(root, 6, '6')
b6.grid(row=1, column=2)

b7 = NumberButton(root, 7, '7')
b7.grid(row=0, column=0)

b8 = NumberButton(root, 8, '8')
b8.grid(row=0, column=1)

b9 = NumberButton(root, 9, '9')
b9.grid(row=0, column=2)


root.mainloop()