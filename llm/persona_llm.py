import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def build_user_persona_llm(cleaned_data, username):
    """
    Generates a user persona for a Reddit user using OpenAI based on cleaned Reddit data.
    Includes citation icons instead of full URLs.
    """
    prompt = f"""
You are an expert user persona analyst.

Generate a detailed user persona for the Reddit user u/{username} based on their Reddit activity.

Follow this structure:
- Name (if possible)
- Age (if inferred or mentioned)
- Location (if inferred or mentioned)
- Occupation (if inferred or mentioned)

Then for each of the following:
- Motivations
- Personality Traits
- Frustrations
- Habits
- Goals & Needs

👉 After each insight or observation, **you MUST** cite the Reddit source using this exact markdown format:
- [🔗](https://reddit.com/example)
- Do NOT include the full URL or any other link format.
- Only use one 🔗 icon per insight.
### Example Output:

- Interested in AI and spatial computing [🔗](https://reddit.com/r/ai/comments/abc)


⚠️ Do NOT show full URLs in the text body. Only use the icon-style link (🔗) to keep it clean.

---

Here is the cleaned Reddit data:
"""

    # Append cleaned posts/comments to the prompt
    for item in cleaned_data:
        url_icon = f"[🔗]({item.get('url')})"
        if item['type'] == 'post':
            prompt += (
                f"\n[POST] Title: {item.get('title')}\n"
                f"Text: {item.get('text')}\n"
                f"Subreddit: {item.get('subreddit')} {url_icon}\n"
            )
        elif item['type'] == 'comment':
            prompt += (
                f"\n[COMMENT] {item.get('body')}\n"
                f"Subreddit: {item.get('subreddit')} {url_icon}\n"
            )

    # Instruction to start generation
    prompt += "\nNow generate the user persona using the content above."

    # Call OpenAI ChatCompletion
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1200,
    )

    return response.choices[0].message.content
