import os

try:
    from google import genai
except Exception:
    genai = None

MODEL_NAME = os.getenv("GEMINI_WORKOUT_MODEL", "gemini-1.5-pro")


def _demo_plan(name: str, age: int, weight: float, goal: str, intensity: str) -> str:
    return f"""7-Day Personalized Workout Plan for {name}

Profile
- Age: {age}
- Weight: {weight:.1f} kg
- Goal: {goal}
- Intensity: {intensity}

Day 1 - Full Body Strength
Warm-up: 8 minutes brisk walking + mobility.
Main workout:
- Bodyweight squats: 3 x 12
- Push-ups: 3 x 8-12
- Glute bridges: 3 x 15
- Dumbbell rows: 3 x 10 each side
Cooldown: 5 minutes easy stretching.

Day 2 - Cardio + Core
Warm-up: 5 minutes.
Main workout:
- Brisk walk/jog: 25 minutes
- Plank: 3 x 30-45 seconds
- Dead bug: 3 x 10 each side
Cooldown: 5 minutes.

Day 3 - Lower Body
Warm-up: 8 minutes.
Main workout:
- Squats: 3 x 12
- Reverse lunges: 3 x 10 each side
- Romanian deadlift: 3 x 10
- Calf raises: 3 x 15
Cooldown: lower-body stretching.

Day 4 - Active Recovery
- Easy walk: 20-30 minutes
- Mobility/yoga: 15 minutes
Keep effort light.

Day 5 - Upper Body + Core
Warm-up: 8 minutes.
Main workout:
- Incline push-ups: 3 x 10
- Dumbbell row: 3 x 10 each side
- Shoulder press: 3 x 10
- Side plank: 3 x 20-30 seconds each side
Cooldown: upper-body stretching.

Day 6 - Cardio Intervals
Warm-up: 8 minutes.
Main workout:
- 5 rounds: 2 minutes moderate + 1 minute easy
- Bird dog: 3 x 10 each side
Cooldown: 5-8 minutes.

Day 7 - Rest / Recovery
- Optional easy walk
- Gentle stretching
- Prioritize sleep and hydration

Progression: increase repetitions, resistance, or duration gradually when the current workload feels manageable.
Safety: stop if you experience pain, dizziness, chest pain, or unusual shortness of breath and seek appropriate professional advice.
"""


def generate_workout_gemini(name, age, weight, goal, intensity):
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key or genai is None:
        return _demo_plan(name, age, weight, goal, intensity)

    try:
        client = genai.Client(api_key=api_key)
        prompt = f"""
Create a structured 7-day fitness plan for:
Name: {name}
Age: {age}
Weight: {weight} kg
Fitness goal: {goal}
Workout intensity: {intensity}

Requirements:
- Label Day 1 through Day 7.
- Include warm-up, main workout, sets/reps or duration, rest guidance, and cooldown/recovery.
- Keep the plan practical and progressive.
- Do not diagnose or treat medical conditions.
- Include a short safety note.
"""
        response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
        return response.text or _demo_plan(name, age, weight, goal, intensity)
    except Exception:
        return _demo_plan(name, age, weight, goal, intensity)
