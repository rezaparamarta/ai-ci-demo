from app import ask_assistant

def test_basic_response():

    result = ask_assistant("What is software testing?")

    assert result is not None
    assert len(result) > 0
