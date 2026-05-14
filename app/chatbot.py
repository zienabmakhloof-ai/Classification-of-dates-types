import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_base = "https://openrouter.ai/api/v1"
openai.api_key = os.getenv("OPENROUTER_API_KEY")


def chat_with_bot(date_type: str) -> str:
    """
    Generate an interesting fact about a given date fruit type
    using an LLM via OpenRouter.

    Args:
        date_type: The name of the date fruit (e.g. 'Ajwa', 'Mejdool').

    Returns:
        A string containing an interesting fact about the date fruit.
    """
    response = openai.ChatCompletion.create(
        model="meta-llama/llama-3.1-70b-instruct:free",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a world-class expert on date palm fruits. "
                    "Generate one interesting fact about the following date fruit type."
                ),
            },
            {"role": "user", "content": date_type},
        ],
    )
    return response.choices[0].message.content


def main():
    print("🤖 Welcome to the Date Fruit Chatbot! (type 'exit' to quit)")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Thanks for chatting! Bye!")
            break
        if not user_input:
            continue
        response = chat_with_bot(user_input)
        print("🤖 Bot:", response)


if __name__ == "__main__":
    main()
