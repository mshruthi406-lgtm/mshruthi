# Phase 8 – Project Demonstration

## Demo Video Script

### 1. Introduction
Say:
“Hello, this is our project, FitBuddy – AI Fitness Plan Generator using Gemini Models.”

### 2. Purpose
Explain:
“FitBuddy accepts basic fitness information and uses generative AI to create a structured 7-day workout plan and a goal-aligned nutrition or recovery tip.”

### 3. Home Page
Show:
- Name
- User ID
- Age
- Weight
- Fitness goal
- Workout intensity

Enter a sample:
- Name: Demo Student
- User ID: FB001
- Age: 20
- Weight: 70
- Goal: muscle gain
- Intensity: high

Click **Generate Plan**.

### 4. Generated Plan
Explain:
“The result page displays the user's profile, a day-wise workout plan with warm-ups, exercises, sets/reps or duration, cooldown/recovery, and a nutrition tip.”

### 5. Feedback
Enter:
“Add more cardio and include one extra recovery day.”

Click **Submit Feedback & Update Plan**.

Explain:
“The feedback is used to revise the existing plan, and the updated plan is stored separately from the original.”

### 6. Admin View
Open `/view-all-users`.
Show:
- User information
- Original plan
- Updated plan
- Delete action

### 7. API Documentation
Open `/docs` and briefly show the FastAPI endpoints.

### 8. Conclusion
Say:
“FitBuddy demonstrates the integration of generative AI, FastAPI, Jinja2 and SQLite to create an adaptive fitness planning workflow.”
