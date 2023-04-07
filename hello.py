import requests
import os
import openai
import creds

url = requests.get("https://api.openai.com/v1/chat/completions")

api = creds.api

prompt = input("Hello! Welcome to Coverletter! Please upload your resume. ")

print(prompt)





