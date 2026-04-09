import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
print("API KEY:", os.getenv("GROQ_API_KEY"))

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    input="Explain the concept of Generative AI",
    model="llama3-70b-8192",
)

print("\nResponse:\n", response.output_text)
