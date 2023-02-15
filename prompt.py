import tkinter as tk
import tkinter.messagebox
import random

prompts = [
	"Will you be my valentine?",
	"Are you stupid?",
	"Is 2+2=8?",
	"Are you enjoying?",
	"Are you in CDT"
]

def show_prompt():
	prompt = random.choice(prompts)
	root = tk.Tk()
	root.withdraw()
	answer = tk.messagebox.askquestion("Random Prompt", prompt)
	if prompt == "Will you be my valentine?" and answer == "yes":
		return
	else:
		show_prompt()

show_prompt()
