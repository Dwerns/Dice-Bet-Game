

#import modules
import random
import tkinter as TK
from tkinter import Button
from tkinter import Radiobutton
from tkinter import Label
from tkinter import Entry
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import Text

#procedure for centering window
def center_window(width=300, height=200):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

#open root window
root = TK.Tk()
center_window(500, 400)
root.geometry("500x400")

#procedure to close window
def close():
	root.quit()

#procedure for the help window	
def instructions():
	messagebox.showinfo("Help","1. You start with $1000\n2. If you guess the dice roll, you win the amount you bet\n3. If you are wrong, you lose the amount you bet\n4. If you go below $0, you lose\n5. You cannot bet more than you have")
	

starting = 1000

#calculation procedure
def calculate():
	global starting
	dice1 = random.randrange(1,7)
	numeric_bet = bet_entry.get()
	numeric_roll = roll_entry.get()
	if numeric_bet.isnumeric() and numeric_roll.isnumeric():
		get_bet_entry=int(numeric_bet)
		get_roll_entry = int(numeric_roll)
		if get_bet_entry > 0 and get_bet_entry <= starting and get_roll_entry > 0 and get_roll_entry <=6:
			if dice1 == get_roll_entry:
				starting = starting + get_bet_entry
				update_total.set('Your total is: $' + str(starting))
				update_roll.set('The dice roll is: ' + str(dice1))
			else:
				starting = starting - get_bet_entry
				if starting > 0:
					update_total.set('Your total is: $' + str(starting))
					update_roll.set('The dice roll is: ' + str(dice1))
				else:
					messagebox.showinfo("Anwer","The number was " + str(dice1) + ". You ran out of money")
					close()
		else:
			messagebox.showinfo("Error","Please enter a valid bet and roll")
	else:
		messagebox.showinfo("Error", "Please enter a valid bet and roll")		
		
#designing bet button 
B2 = Button(root,text = "Bet", padx=50, command = calculate)
B2.place(x=25, y = 350)

#designing close button
close_button = Button(root,text = "Close", padx = 50,command = close)
close_button.place(x = 176,y = 350)

#designing instructions button
help_button = Button(root, text = "Help", padx = 50, command = instructions)
help_button.place(x = 340, y = 350)

#inserting picture
logo = PhotoImage(file="dice.gif")
logo = logo.subsample(2, 2)
image_label = Label(root, image = logo).place(x = 75, y= 0)

#designing entry labels
bet_entry_label = Label(root, text="Enter Bet:").place(x=75,y=250)
roll_entry_label = Label(root, text="Guess roll:").place(x=75,y=300)

#declaring 'update_total' to set the amount to a label
update_total = TK.StringVar()
update_total.set('Your total is: $1000 ')
output = Label(root, textvariable = update_total).place(x=250,y=250)

#declaring 'update_roll' to set the roll to label
update_roll = TK.StringVar()
update_roll.set('The dice roll is: ')
output_roll = Label(root, textvariable = update_roll).place(x=250,y=300)

#designing entry input
bet_entry = Entry(root)
bet_entry.place(x=150, y=250, width=50)
roll_entry = Entry(root)
roll_entry.place(x=150, y=300, width=50)
root.mainloop()



