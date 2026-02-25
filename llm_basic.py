from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

open_api_key = os.getenv("openaikey")
if open_api_key is None:
    print("Error: OPENAIKEY not found in .env file.")
else:
    try:
        openai_client = OpenAI(api_key=open_api_key)
        print("Connected Successfully")
    except Exception as e:
        print(f"An error occurred during OpenAI client initialization: {e}")

my_message = "write a story for youtube short for kids."
print(f"sending message to open ai: '{my_message}'")

response = openai_client.chat.completions.create(model="gpt-4o-mini",
                                                 messages='write a story for youtube short for kids.')

print(response)
print(response.choice[0].message.content)