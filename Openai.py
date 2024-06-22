import os
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise OpenAIError("The OPENAI_API_KEY environment variable is not set")

client = OpenAI(api_key=api_key)

system_message = {"role": "system", "content": "You are a cyber expert."}
user_message = {"role": "user", "content": "Write a random python script."}

try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[system_message, user_message]
    )
    
    completion_ = response.choices[0].message['content']
    print(completion_)
except OpenAIError as e:
    print(f"OpenAI API error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
