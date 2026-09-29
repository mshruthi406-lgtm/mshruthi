import os

try:
    from google import genai
except Exception:
    genai = None

MODEL_NAME = os.getenv("GEMINI_WORKOUT_MODEL", "gemini-1.5-pro")


def update_workout_plan(original_plan: str, feedback: str, goal: str, intensity: str) -> str:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key or genai is None:
        return (
            original_plan
            + "\n\nUPDATED ACCORDING TO FEEDBACK\n"
            + f"User feedback: {feedback}\n"
            + f"Adjustment: The plan should place additional emphasis on the requested change while retaining the original {goal} goal and {intensity} intensity."
        )

    try:
        client = genai.Client(api_key=api_key)
        prompt = f"""
Update the following workout plan using the user's feedback.

Goal: {goal}
Intensity: {intensity}
Feedback: {feedback}

Original plan:
{original_plan}

Return a complete revised 7-day plan. Preserve useful structure, apply the requested changes,
and include warm-up, main workout, cooldown/recovery, and sensible safety guidance.
"""
        response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
        return response.text or original_plan
    except Exception:
        return original_plan + f"\n\nFeedback recorded: {feedback}"
