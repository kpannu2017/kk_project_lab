#!/usr/bin/env python3
"""
Haute Food Fusion — local dev server
Run: python server.py
Open: http://localhost:5000
"""

import os
import json
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import anthropic
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder=BASE_DIR)
CORS(app)

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

SKILL_LABELS = {
    "home": "Home Cook",
    "confident": "Confident Cook",
    "chef": "Chef-Level",
}

SKILL_CONTEXT = {
    "home": "weeknight techniques — sautéing, boiling, roasting, simple pan sauces",
    "confident": "intermediate techniques — braising, deboning, scratch sauces, multi-component dishes",
    "chef": "advanced techniques — fermentation, multi-stage preparations, precision temperatures, specialty equipment",
}

SYSTEM_PROMPT = (
    "You are an elite culinary AI specializing in original fusion cuisine. "
    "You invent dishes that authentically draw from multiple culinary traditions, "
    "creating something entirely new that could genuinely appear on a high-end restaurant menu. "
    "You understand flavor profiles, technique compatibility, and ingredient synergy across world cuisines. "
    "Always respond with valid JSON only — no markdown fences, no commentary outside the JSON object."
)


@app.route("/")
def index():
    return send_from_directory(BASE_DIR, "app.html")


@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(BASE_DIR, filename)


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json(force=True)
    cuisines: list = data.get("cuisines", [])
    ingredients: str = data.get("ingredients", "").strip()
    skill: str = data.get("skill", "home")

    if len(cuisines) < 2:
        return jsonify({"success": False, "error": "Select at least 2 cuisines"}), 400

    cuisine_list = ", ".join(cuisines)
    skill_label = SKILL_LABELS.get(skill, "Home Cook")
    skill_desc = SKILL_CONTEXT.get(skill, SKILL_CONTEXT["home"])
    ing_text = ingredients if ingredients else "standard pantry staples"

    prompt = f"""Create an original fusion dish that authentically blends {cuisine_list} culinary traditions.

Chef skill level: {skill_label} — {skill_desc}

Available ingredients: {ing_text}

Invent a dish that feels genuinely original — not a superficial ingredient swap. \
The name should be evocative and may blend language elements from the source cuisines. \
The recipe must be executable at the stated skill level.

Return a single JSON object with exactly this structure:
{{
  "name": "Creative fusion dish name",
  "tagline": "One elegant sentence — the dish's essence in under 20 words",
  "time": "Total time including prep (e.g. '45 min' or '2 hrs 30 min')",
  "skill": "{skill_label}",
  "ingredients": [
    "Quantity + ingredient (e.g. '400g skin-on chicken thighs')",
    "..."
  ],
  "steps": [
    "Full step instruction with technique details",
    "..."
  ],
  "plating": "2–3 sentences of precise plating direction: exact placement, sauce application, garnish, and visual composition."
}}

Requirements:
- 8–12 ingredients, prioritising the user's available ingredients
- 4–7 cooking steps, each a full paragraph with technique detail
- Plating must be specific and visual — describe it as a chef briefing a line cook"""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1500,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}],
        )

        raw = message.content[0].text.strip()
        # Strip accidental markdown fences
        if raw.startswith("```"):
            parts = raw.split("```")
            raw = parts[1].lstrip("json").strip() if len(parts) > 1 else raw

        recipe = json.loads(raw)
        # Enforce correct skill label regardless of what Claude returned
        recipe["skill"] = skill_label

        return jsonify({"success": True, "recipe": recipe})

    except json.JSONDecodeError:
        return jsonify({"success": False, "error": "AI returned malformed JSON — try again"}), 500
    except anthropic.APIError as e:
        return jsonify({"success": False, "error": f"Anthropic API error: {e}"}), 502
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/substitute", methods=["POST"])
def substitute():
    data = request.get_json(force=True)
    ingredient: str = data.get("ingredient", "").strip()
    recipe_name: str = data.get("recipe_name", "").strip()

    if not ingredient:
        return jsonify({"success": False, "error": "No ingredient provided"}), 400

    context = f' in "{recipe_name}"' if recipe_name else ""
    prompt = (
        f'A cook doesn\'t have {ingredient}{context}. '
        f"Suggest the best substitute and explain in 1–2 sentences why it works for this dish. Be specific and practical."
    )

    try:
        message = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=180,
            messages=[{"role": "user", "content": prompt}],
        )
        return jsonify({"success": True, "suggestion": message.content[0].text.strip()})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == "__main__":
    key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not key or not key.startswith("sk-ant-"):
        print("ERROR: ANTHROPIC_API_KEY not set in .env")
        raise SystemExit(1)
    print("Haute Food Fusion server starting...")
    print("   Open http://localhost:5000 in your browser")
    app.run(debug=True, port=5000)
