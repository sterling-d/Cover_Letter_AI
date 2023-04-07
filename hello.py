import requests
import os
import openai
import creds
from tkinter import filedialog
from tkinter import *

url = requests.get("https://api.openai.com/v1/chat/completions")

prompt = input("Hello! Welcome to Coverletter! Please press the Enter key to begin.")

# create a Tkinter window
root = Tk()
root.withdraw() # hide the root window

# ask the user to select a file
file_path = filedialog.askopenfilename()

# print the file path
print("Selected file:", file_path)





