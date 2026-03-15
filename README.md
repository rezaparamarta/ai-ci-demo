# AI CI/CD Testing Pipeline with CircleCI

This project demonstrates how to build an **automated CI/CD pipeline for testing an AI-powered application** using **CircleCI, Python, and Pytest**.

The pipeline automatically runs tests on every commit to validate the behavior of an AI assistant powered by the OpenAI API.

This project highlights how **QA Engineers can implement automated testing pipelines for AI systems**.

---

# 🚀 Project Overview

Modern AI applications require automated validation to ensure that model responses remain correct, stable, and reliable after each code change.

This project implements a **Continuous Integration pipeline** that:

* Installs project dependencies
* Runs automated tests
* Calls the OpenAI API
* Validates AI responses
* Reports success or failure automatically

All tests are executed automatically through **CircleCI pipelines** whenever changes are pushed to the repository.

---

# 🧠 Use Case

AI systems can degrade over time when prompts or models change. This pipeline ensures:

* AI responses remain valid
* Critical keywords appear in responses
* The assistant continues to behave correctly

This is an example of **AI Regression Testing**.

---

# 🏗 Project Architecture

```
ai-ci-demo
│
├── .circleci/
│   └── config.yml          # CircleCI pipeline configuration
│
├── app.py                  # AI assistant using OpenAI API
├── test_assistant.py       # Basic AI response test
├── test_release_evals.py   # AI evaluation tests
│
├── requirements.txt        # Python dependencies
└── utils.py                # Helper utilities
```

---

# ⚙️ CI/CD Pipeline Workflow

Every time a commit is pushed to GitHub:

```
git push
   ↓
CircleCI Pipeline Triggered
   ↓
Checkout Repository
   ↓
Install Dependencies
   ↓
Run Pytest
   ↓
Call OpenAI API
   ↓
Validate AI Response
```

If tests pass:

```
Pipeline Status: SUCCESS
```

If tests fail:

```
Pipeline Status: FAILED
```

---

# 🧪 Example AI Test

Example test that validates AI output:

```python
from app import ask_assistant

def test_ai_response():

    result = ask_assistant("What is CI/CD?")

    assert result is not None
    assert len(result) > 0
```

This test ensures the AI system always returns a valid response.

---

# 🔐 Environment Variables

The project requires an OpenAI API key stored securely in CircleCI.

Environment variable used:

```
OPENAI_API_KEY
```

This key is configured in:

```
CircleCI → Project Settings → Environment Variables
```

This ensures API keys are never exposed in the repository.

---

# 🛠 Technologies Used

* Python
* OpenAI API
* Pytest
* CircleCI
* GitHub

---

# 📊 What This Project Demonstrates

This project demonstrates several important QA and DevOps practices:

* Continuous Integration for AI applications
* Automated testing of LLM responses
* API-based test automation
* Secure environment variable management
* CI/CD pipelines for AI systems

---

# 🔮 Future Improvements

Possible enhancements for this project include:

* Prompt testing framework
* AI hallucination detection
* LLM evaluation scoring
* Automated AI regression testing
* Dataset-based prompt validation

---

# 👨‍💻 Author

**Reza Paramarta**

QA Engineer interested in:

* AI Testing
* Automation Testing
* LLM Evaluation
* CI/CD for AI systems

GitHub:
https://github.com/rezaparamarta
