import requests
import os
import creds
from tkinter import filedialog
from tkinter import *

#url = f"https://api.openai.com/v1/chat/completions"


import openai

# Getting error message when utilizing API key from OpenAI

openai.api_key = "{{SECRET_KEY}}"

try:
    print(openai.Model.list())
except Exception as e:
    print(f"Error: {e}")

#response = requests.get(url)


#requests.get("https://api.openai.com/v1/chat/completions")

#f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

#prompt = input("Hello! Welcome to Coverletter! Please press the Enter key to upload your resume.")

# create a Tkinter window
#root = Tk()
#root.withdraw() # hide the root window

# ask the user to select a file
#file_path = filedialog.askopenfilename()

# print the file path
#print("Selected file:", file_path)


#url = input("Enter website URL: ")

#response = requests.get(url)




