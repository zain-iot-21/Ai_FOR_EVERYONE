from openai import OpenAI
from apikey import  apikey
import os


os.environ["OPENAI_API_KEY"] = apikey

OpenAI.api_key = apikey

client = OpenAI()
prompt = "Which is the largest city on Earth?"

response = client.chat.completions.create(
    model = 'gpt-4-0125-preview',
    messages = [{"role":"user", "context" : prompt}])
print(response)
print(response.choices[0].message.content)