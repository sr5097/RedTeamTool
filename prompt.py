# Importing the necessary modules
import tkinter as tk
import tkinter.messagebox
import random

# List of random prompts
prompts = [
	"Will you be my valentine?",
	"Are you stupid?",
	"Is 2+2=8?",
	"Are you enjoying?",
	"Are you in CDT"
]

'''
Defined a function to generate a random prompt and display it in a pop-up window.
If it's a certain question nd the answer selected is yes, the prompts will stop. 
Otherwise, the prompts will continue to pop up.
'''
def show_prompt():
	prompt = random.choice(prompts)		# Selects a random prompt from the list of prompts
	root = tk.Tk()		# Creates a new tkinter window
	root.withdraw()		# Hiding tkinter window
	answer = tk.messagebox.askquestion("Random Prompt", prompt)		#Asking the prompt as a message box
	# If the prompt is the valentine prompt and the answer is yes, return without showing more prompts
	if prompt == "Will you be my valentine?" and answer == "yes":	
		return
	# If the answer is no or the prompt is not the valentine prompt, show more prompts
	else:
		show_prompt()

# Function call
show_prompt()
