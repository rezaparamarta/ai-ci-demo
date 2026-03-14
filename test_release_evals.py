from app import ask_assistant


def test_ai_quality():

    result = ask_assistant("What is CI/CD?")

    assert "continuous" in result.lower()
