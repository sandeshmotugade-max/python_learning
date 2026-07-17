from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

# One-Shot Prompt
prompt = """
Classify the sentiment of a review.

Example:

Review: I love this mobile phone.
Sentiment: Positive

Now classify the following:

Review: The battery drains very quickly.
Sentiment:
"""

try:
    response = client.chat.completions.create(
        model="openai/gpt-5",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print("AI Response:")
    print(response.choices[0].message.content)

except Exception as e:
    print("Error:", e)