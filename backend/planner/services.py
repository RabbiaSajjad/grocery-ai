from openai import OpenAI
import json
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_grocery_plan(prompt, pantry_items):

    pantry_text = ", ".join(pantry_items)

    system_prompt = f"""
You are a grocery planning assistant.

Available pantry items:
{pantry_text}

Return JSON ONLY:

{{
  "meal_plan": [],
  "grocery_list": [],
  "estimated_cost": 0
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
    )

    return json.loads(
        response.choices[0].message.content
    )