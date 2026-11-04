# Project Summary: AI Student Assistant Backend

## 1. Overview

**Project Name:** `gmc_fast_ai04112026`  
**Framework:** FastAPI with Pydantic for data validation  
**Purpose:** An AI-powered student assistant backend providing interactive learning tools such as chat assistance, quiz generation, text summarization, and flashcard creation.

---

## 2. Project Structure

```text
gmc_fast_ai04112026/
├── .venv/                  # Virtual environment
├── .env                    # Environment variables (e.g., API keys)
├── .env.example            # Sample environment variables
├── requirements.txt        # Project dependencies
├── test.py                 # Pydantic schema tests and experiments
├── main.py                 # Initial / minimal FastAPI backend implementation
├── main1.py                # Expanded API with validation, quizzes, summaries & flashcards
├── README.md               # Repository documentation
└── summarize.md            # Project and endpoint summary
```

---

## 3. Dependencies

From `requirements.txt`:
- **`fastapi`**: Web framework for building high-performance RESTful APIs.
- **`uvicorn`**: ASGI web server to run the FastAPI application.
- **`pydantic`**: Data parsing, typing, and input validation.
- **`openai`**: Official client for LLM integration (OpenAI API).
- **`python-dotenv`**: Loads environment variables from `.env`.
- **`httpx`**: Asynchronous HTTP client for testing and external requests.
- **`pytest` & `pytest-asyncio`**: Test framework for unit and asynchronous integration tests.

---

## 4. API Endpoints & Data Models (`main1.py`)

### 4.1 General / Informational Endpoints

| Method | Endpoint | Description | Sample Response |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Root endpoint / Welcome message | `{"status": "ok", "message": "Welcome To the AI Assistant backend"}` |
| `GET` | `/about` | Project description and title | `{"status": "ok", "Title": "AI Student assistant", "Description": "it helps students"}` |
| `GET` | `/health` | Health check endpoint | `{"status": "ok", "version": "0.1.0"}` |

---

### 4.2 Interactive & AI Endpoints

#### `POST /chat`
Provides conversational assistant responses.

- **Request Model:** `ChatRequest`
  ```json
  {
    "message": "Explain the concept of inheritance in OOP"
  }
  ```
- **Response Format:**
  ```json
  {
    "answer": "You asked for Explain the concept of inheritance in OOP",
    "model": "placeholder",
    "tokens": 0
  }
  ```

---

#### `POST /quizz`
Generates practice quiz questions on a given topic with constraints on question counts and options.

- **Request Model:** `QuizzRequest`
  - `subject` (`str`): Minimum 3 characters (`min_length=3`).
  - `number_quizzes` (`int`): Range between 2 and 9 (`gt=1, lt=10`).
  - `number_options` (`int`): Range between 3 and 4 (`gt=2, lt=5`).
  ```json
  {
    "subject": "Python Basics",
    "number_quizzes": 5,
    "number_options": 4
  }
  ```
- **Response Format:**
  ```json
  {
    "topic": "Python Basics",
    "quizzes": [
      {
        "question": "What is a list comprehension?",
        "options": ["Option A", "Option B", "Option C", "Option D"],
        "correct_answer": 0
      }
    ]
  }
  ```

---

#### `POST /summarize`
Generates a concise summary for a study topic or text.

- **Request Model:** `SummarizeQuest`
  ```json
  {
    "topic": "Machine Learning Fundamentals"
  }
  ```
- **Response Format:**
  ```json
  {
    "topic": "Machine Learning Fundamentals",
    "summary": "This is summary"
  }
  ```

---

#### `GET /flashcard`
Generates flashcards for revision.

- **Request Model:** `FlashCard`
  - `cours` (`str`): Course or module title.
  - `number_flashcards` (`int`): Number of cards to create.
- **Response Format:**
  ```json
  {
    "topic": "Course Name",
    "flashcards": ["a", "b", "c"]
  }
  ```

---

## 5. How to Run the Application

### 5.1 Activate the Virtual Environment
```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

### 5.2 Start the Server
Run using Uvicorn with auto-reload enabled:

```powershell
uvicorn main1:app --reload --port 8000
```

### 5.3 Interactive Documentation
Once started, open your browser to test endpoints directly:
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 6. Recommended Improvements & Fixes for `main1.py`

1. **Decorator Syntax:**  
   In `main1.py`, lines 58 and 74 have `app.get(...)` instead of `@app.get(...)`. Add the `@` decorator symbol so FastAPI registers the routes properly.
2. **HTTP Method for Body Payloads:**  
   In HTTP standards, `GET` requests should generally not include request bodies. Consider switching `/flashcard` from `GET` to `POST` (`@app.post("/flashcard")`).
3. **Attribute Consistency:**  
   In `flashcard()` in `main1.py`, `request.cours` is defined in `FlashCard`, but the return dictionary attempts to access `request.topic`. Update it to `request.cours`.
4. **OpenAI Integration:**  
   Connect the placeholder responses in `/chat`, `/quizz`, and `/summarize` to the OpenAI client using the `openai` package and API keys loaded from `.env`.

