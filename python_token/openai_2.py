import openai
import os

API_KEY = os.getenv("OPENROUTER_API_KEY", "")

client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
    default_headers={
        "HTTP-Referer": "http://localhost",
        "X-Title": "Beginner Travel Planner"
    }
)
# System prompt (defines behavior)
messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful AI travel planner. "
            "You suggest destinations, budgets, and simple itineraries. "
            "Keep answers beginner-friendly and practical."
            "ASK 3 Questions, Budget? Days? Number of Persons?"
            "Keep answers short. 20 words output"
        )
    }
]
print(" AI Travel Planner (type 'exit' to quit)\n")
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye ")
        break

    messages.append({"role": "user", "content": user_input})
    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=messages
        )
        reply = response.choices[0].message.content

    except Exception as e:
        reply = f" Error: {str(e)}"

    print("\n AI Agent :", reply, "\n")
    
    messages.append({"role": "assistant", "content": reply})
    
    # Keep only last few messages (avoid token overload)
    if len(messages) > 8:
        messages = [messages[0]] + messages[-7:]