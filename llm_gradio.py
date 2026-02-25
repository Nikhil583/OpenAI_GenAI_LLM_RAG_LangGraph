from openai import OpenAI
from dotenv import load_dotenv
import os
import gradio as gr

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

# def greet(name):
#     return "Hello " + name + "!"

# demo = gr.Interface(fn=greet, inputs="text", outputs="text")
# demo.launch()

def get_ai_tutor_response(user_question):
    system_prompt = "You are a helpful and patient AI Tutor. Explain Concepts clearly and concisely"

    try:
        response = openai_client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [
                {"role":"system","content":system_prompt},
                {"role":"user","content":user_question}
            ],
            temperature = 0.7
        )
        ai_response = response.choices[0].message.content
        return ai_response
    except Exception as e:
        print(f"{e}")
        return f"Sorry, I encountered an error trying to get an answer: {e}"
    
def stream_ai_tutor_response(user_question):
    system_prompt = "You are a helpful and patient AI Tutor. Explain Concepts clearly and concisely"

    try:
        stream = openai_client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [
                {"role":"system","content":system_prompt},
                {"role":"user","content":user_question}
            ],
            temperature = 0.7,
            stream = True,
        )

        full_response = ""
        for chunk in stream:
            if chunk.choices[0].delta and chunk.choices[0].delta.content:
                text_chunk = chunk.choices[0].delta.content
                full_response += text_chunk
                yield full_response

    except Exception as e:
        print(f"{e}")
        yield f"Sorry, I encountered an error trying to get an answer: {e}"

explanation_level = {
    1: "Like I'm 5 years old",
    2: "Like I'm 10 years old",
    3: "Like a high school student",
    4: "Like a college student",
    5: "like an expert in the field",
}

def stream_ai_tutor_response_with_level(user_question,exp_level):

    level_desc = explanation_level.get(exp_level,"clearly and concisely")
    system_prompt = f"You are a helpful and patient AI Tutor. Explain Concepts with experence level {level_desc}"

    try:
        stream = openai_client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = [
                {"role":"system","content":system_prompt},
                {"role":"user","content":user_question}
            ],
            temperature = 0.7,
            stream = True,
        )

        full_response = ""
        for chunk in stream:
            if chunk.choices[0].delta and chunk.choices[0].delta.content:
                text_chunk = chunk.choices[0].delta.content
                full_response += text_chunk
                yield full_response

    except Exception as e:
        print(f"{e}")
        yield f"Sorry, I encountered an error trying to get an answer: {e}"


# gradi_ui = gr.Interface(
#     fn = stream_ai_tutor_response,
#     inputs = gr.Textbox(lines = 2, placeholder = "Ask the AI Tutor anything...", label = "Your Question"),
#     outputs = gr.Markdown(
#         label = "AI tutor's Answer",
#         container = True,
#         height = 250
#         ),
#     title = "Simple AI Tutor",
#     description = "Enter the question and get you answer")
# print("Launching UI")
# gradi_ui.launch()

gradio_stream_level = gr.Interface(
    fn = stream_ai_tutor_response_with_level,
    inputs = [
        gr.Textbox(lines = 2, placeholder = "Ask the AI Tutor anything...", label = "Your Question"),
        gr.Slider(
            minimum = 1,
            maximum = 5,
            step = 1,
            value = 3,
            label = "Explanation Level"
        )
    ],
    outputs = gr.Markdown(
        label = "AI tutor's Answer",
        container = True,
        height = 250
        ),
    title = "Simple AI Tutor",
    description = "Enter the question and get you answer")
print("Launching UI")
gradio_stream_level.launch()