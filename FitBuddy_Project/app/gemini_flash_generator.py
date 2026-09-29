import os

try:
    from google import genai
except Exception:
    genai = None

MODEL_NAME = os.getenv("GEMINI_TIP_MODEL", "gemini-1.5-flash")


def _demo_tip(goal: str) -> str:
    goal_lower = goal.lower()
    if "muscle" in goal_lower:
        return "Prioritize a protein-rich food at each meal, stay hydrated, and include adequate recovery between challenging sessions."
    if "weight" in goal_lower or "fat" in goal_lower:
        return "Build meals around vegetables, protein, whole-food carbohydrates, and sensible portions; hydration and consistent sleep also support training."
    if "flex" in goal_lower or "mobility" in goal_lower:
        return "Include regular hydration and a variety of fruits, vegetables, protein sources, and healthy fats while keeping mobility work gentle and consistent."
    return "Prioritize balanced meals with protein, vegetables, whole-food carbohydrates, healthy fats, hydration, and sufficient sleep."


def generate_nutrition_tip_with_flash(goal: str) -> str:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key or genai is None:
        return _demo_tip(goal)

    try:
        client = genai.Client(api_key=api_key)
        prompt = f"Give one concise, practical nutrition or recovery tip for someone whose fitness goal is: {goal}. Avoid medical claims."
        response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
        return response.text or _demo_tip(goal)
    except Exception:
        return _demo_tip(goal)
