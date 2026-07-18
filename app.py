import os
import gradio as gr
from google import genai

# Read Gemini API key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Please set the GEMINI_API_KEY environment variable.")

client = genai.Client(api_key=API_KEY)


def convert_code(source_language, target_language, code):
    if not code.strip():
        return "Please enter some source code."

    prompt = f"""
You are an expert programming language translator.

Convert the following {source_language} code into {target_language}.

Requirements:
- Preserve the original logic exactly.
- Use proper syntax and best coding practices.
- Add comments where appropriate.
- Ensure the code is complete and executable.
- Return only the converted code inside a code block.

Source Language: {source_language}
Target Language: {target_language}

Code:
```{source_language.lower()}
{code}

"""

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

except Exception as e:
    return f"Error: {e}"

demo = gr.Interface(
fn=convert_code,
inputs=[
gr.Dropdown(
choices=[
"Python",
"Java",
"C",
"C++",
"JavaScript",
"C#",
"Go",
"PHP"
],
value="Python",
label="Source Language"
),
gr.Dropdown(
choices=[
"Python",
"Java",
"C",
"C++",
"JavaScript",
"C#",
"Go",
"PHP"
],
value="Java",
label="Target Language"
),
gr.Textbox(
lines=20,
label="Source Code",
placeholder="Paste your source code here..."
)
],
outputs=gr.Textbox(
lines=20,
label="Converted Code"
),
title="💻 AI Programming Language Converter",
description="Convert code between programming languages using Google's Gemini AI.",
theme=gr.themes.Soft()
)

if name == "main":
demo.launch(debug=True)
