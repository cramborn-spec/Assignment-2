"""
main.py 

Setup:
    pip install groq
    Set your GROQ_API_KEY environment variable before running:
        export GROQ_API_KEY="your_api_key_here"

Usage:
    python main.py
"""

import os
from groq import Groq

def main():
    # Initialize the Groq client (reads GROQ_API_KEY from environment)
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    # Keep conversation history for multi-turn context
    conversation_history = []

    print("Welcome! Ask me anything. Type 'quit' to exit.\n")

    while True:
        # Get user input
        user_input = input("You: ").strip()

        # Exit condition
        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        # Skip empty input
        if not user_input:
            continue

        # Append user message to conversation history
        conversation_history.append({
            "role": "user",
            "content": user_input,
        })

        # Call the Groq API
        chat_completion = client.chat.completions.create(
            messages=conversation_history,
            model="llama3-8b-8192",  # Fast, capable Llama 3 model on Groq
        )

        # Extract the assistant's reply
        assistant_message = chat_completion.choices[0].message.content

        # Append assistant reply to conversation history
        conversation_history.append({
            "role": "assistant",
            "content": assistant_message,
        })

        print(f"\nAssistant: {assistant_message}\n")


if __name__ == "__main__":
    main()
