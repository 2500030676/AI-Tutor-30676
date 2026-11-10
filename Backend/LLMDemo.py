from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API KEY:", api_key)

client = genai.Client(api_key=api_key)

print("===== AI TUTOR USING GEMINI =====")

question = input("Enter your question: ")

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=question
)

print(response.text)