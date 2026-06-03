import json
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def generate_grocery_plan(user_prompt, pantry_items):
    pantry_text = ", ".join(pantry_items) if pantry_items else "No pantry items provided"

    prompt = f"""
You are an AI grocery planning assistant.

Rules:
- Use pantry items first.
- Keep meals budget-friendly.
- Avoid food waste.
- Return valid JSON only.
- Do not include markdown.

Available pantry items:
{pantry_text}

User request:
{user_prompt}

Return JSON in this exact structure:
{{
  "meal_plan": [
    {{
      "day": "Day 1",
      "meals": ["meal name"]
    }}
  ],
  "grocery_list": [
    {{
      "item": "item name",
      "quantity": "quantity",
      "category": "category",
      "estimated_price": 0
    }}
  ],
  "estimated_total_cost": 0,
  "budget_tips": ["tip"]
}}
"""

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(prompt)

    cleaned_text = response.text.strip()

    if cleaned_text.startswith("```json"):
        cleaned_text = cleaned_text.replace("```json", "").replace("```", "").strip()

    return json.loads(cleaned_text)