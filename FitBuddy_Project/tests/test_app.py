from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home_page():
    response = client.get("/")
    assert response.status_code == 200
    assert "FitBuddy" in response.text


def test_generate_plan():
    response = client.post(
        "/generate-workout",
        data={
            "name": "Demo Student",
            "user_id": "TEST001",
            "age": "20",
            "weight": "70",
            "goal": "muscle gain",
            "intensity": "medium",
        },
    )
    assert response.status_code == 200
    assert "Workout Plan" in response.text
    assert "Demo Student" in response.text


def test_feedback():
    client.post(
        "/generate-workout",
        data={
            "name": "Feedback Student",
            "user_id": "TEST002",
            "age": "21",
            "weight": "65",
            "goal": "weight loss",
            "intensity": "low",
        },
    )
    response = client.post(
        "/submit-feedback",
        data={"user_id": "TEST002", "feedback": "Add more cardio and one rest day."},
    )
    assert response.status_code == 200
    assert "updated" in response.text.lower()
