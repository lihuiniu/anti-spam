import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def is_spam_llm(text: str) -> bool:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                { "role": "system", "content": "You are a spam classifier. Reply only with 'yes' if the message is spam, otherwise 'no'." },
                { "role": "user", "content": text }
            ],
            temperature=0
        )
        result = response['choices'][0]['message']['content'].strip().lower()
        return result == "yes"
    except Exception as e:
        print("LLM spam check failed:", e)
        return False
