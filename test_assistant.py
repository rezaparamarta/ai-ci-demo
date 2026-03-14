from app import ask_assistant

def test_ai_response():

    result = ask_assistant("What is CI/CD?")

    assert result is not None
    assert len(result) > 0
