import requests
import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question) :
    response = model.generate_content(question)
    return response.text


question = input("ENTERHT THE QUESTION: ")
data_value = get_gemini_response(question)
print(data_value)