from openai import OpenAI
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

open_api_key = os.getenv("openaikey")
if open_api_key is not None:
    try:
        openai_client = OpenAI(api_key = open_api_key)
        print("Connected to OpenAI Successfully")
    except Exception as e:
        print(f"{e}")
else:
    print("Key Not Found.")

# print(open_api_key[:15])

img_path = r"C:\Users\nikhi\OneDrive\Desktop\LLM_Course\img.webp"
img = Image.open(img_path)
print(img.format)
print(img.size)
print(img.mode)

# display(img)
img_to_analyze = img

my_message = f"what is in the image: {img}"

response = openai_client.chat.completions.create(model = "gpt-4o-mini", 
                                                 messages = [{"role" : "user", "content" : my_message}])

print(response)
print(response.choice[0].message.content)
