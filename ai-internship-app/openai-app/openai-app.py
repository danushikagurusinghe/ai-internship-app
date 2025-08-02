import os
import openai
from dotenv import load_dotenv

# Load the OpenAI API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("OpenAI API key not found in .env file.")
    exit(1)

openai.api_key = api_key

def get_fun_fact(place):
    prompt = (
        f"Tell me a fun, interesting, and lesser-known fact about {place}. "
        "Make it engaging and concise."
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "system", "content": "You are a helpful assistant that provides fun facts about places."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0.8,
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {e}"

def main():
    place = input("Enter a city or country: ").strip()
    fact = get_fun_fact(place)
    print(f"\nFun fact about {place}:\n{fact}")

if __name__ == "__main__":
    main()

    