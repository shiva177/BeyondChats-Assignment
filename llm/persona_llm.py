import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def build_user_persona_llm(cleaned_data, username):
    prompt = f"""
You are an expert user persona analyst.

Generate a detailed user persona for the Reddit user u/{username} based on their cleaned Reddit activity.
Use this structure and cite Reddit URLs where relevant:

## Sample Structure:
Name: [Optional]
Age: [Inferred or mentioned]
Location: [Inferred or mentioned]
Occupation: [Inferred or mentioned]
Motivations: [...]
Personality Traits: [...]
Frustrations: [...]
Behavior & Habits: [...]
Goals & Needs: [...]

## Cleaned Reddit Content:
"""

    for item in cleaned_data:
        if item['type'] == 'post':
            prompt += f"\n[POST] Title: {item.get('title')}\nText: {item.get('text')}\nSubreddit: {item.get('subreddit')}\nURL: {item.get('url')}\n"
        elif item['type'] == 'comment':
            prompt += f"\n[COMMENT] {item.get('body')}\nSubreddit: {item.get('subreddit')}\nURL: {item.get('url')}\n"

    prompt += "\nNow generate the user persona using the content above."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1200,
    )

    return response.choices[0].message.content
