# Python Practice

This repository contains my hands-on practice of core Python concepts as part of my coursework.
Each file focuses on a specific topic and includes small experiments and examples.

---

## 📚 Topics Covered

* Python Dictionaries
* Dictionary Methods (keys, values, items, update, pop)
* Decision Making (if-else statements)
* For Loops and While Loops
* Loops with Dictionaries
* Type Casting (string ↔ integer)
* List Comprehension
* List Slicing
* NumPy Basics
* Introduction to APIs and FastAPI

---

## 📁 Repository Structure

```
python-practice
│
├ dictionary_examples.py
├ loops_practice.py
├ dictionary_with_loops.py
├ list_comprehension.py
├ slicing_examples.py
├ numpy_practice.py
├ fastapi_ai_helper.py
└ README.md
```

---

## 🚀 FastAPI Mini Project

I built a simple FastAPI application that takes a topic as input and returns a one-line explanation.

### 🔹 Features

* Built using FastAPI
* Uses POST request
* Accepts user input (topic)
* Returns a generated response

---

## ▶️ How to Run the FastAPI App

1. Install dependencies:

```
python -m pip install fastapi uvicorn
```

2. Run the server:

```
uvicorn fastapi_ai_helper:app --reload
```

3. Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Example API Request

```json
{
  "topic": "Machine Learning"
}
```

## ✅ Example API Response

```json
{
  "answer": "Machine Learning is a concept used in technology to solve problems and improve efficiency."
}
```

---

## 💡 Learning Outcome

Through this repository, I practiced:

* Writing clean and structured Python code
* Understanding core programming concepts
* Working with loops, conditions, and data structures
* Exploring APIs and building a basic FastAPI application
* Gaining hands-on experience with real-world coding workflows

---

## 📌 Note

This repository is part of my continuous learning process, and I will keep updating it with more concepts and examples.
