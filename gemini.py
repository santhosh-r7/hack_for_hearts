import google.generativeai as genai
import os

genai.configure(api_key="")
model = genai.GenerativeModel('gemini-1.5-flash')

prompt = x+" explain any tecnical or medical terms in original words with explanation in bracket"

response = model.generate_content(prompt)

print(response.text)
