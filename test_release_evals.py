from app import ask_assistant

def test_contains_ci_cd():

    result = ask_assistant("Explain CI/CD briefly")

    assert "continuous" in result.lower()
