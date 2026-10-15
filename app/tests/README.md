# DevFlow AI 🚀

AI-Powered Software Engineering Platform

DevFlow AI is a Python-based backend application that analyzes
Python code and identifies basic code-quality issues.

## Features

- Analyze Python code
- Detect syntax errors
- Identify functions and classes
- Count lines of code
- Detect long lines
- Identify TODO comments
- REST API built with FastAPI
- Automated tests using Pytest

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pytest
- HTTPX

## Project Structure

    devflow-ai/
    ├── app/
    │   ├── main.py
    │   └── analyzer.py
    ├── tests/
    │   ├── test_analyzer.py
    │   └── test_api.py
    ├── requirements.txt
    └── README.md

## Installation

Create and activate a virtual environment:

    python -m venv .venv

On Windows PowerShell:

    .venv\Scripts\Activate.ps1

Install dependencies:

    python -m pip install -r requirements.txt

## Run the Application

    python -m uvicorn app.main:app --reload

Open the API documentation in your browser:

    http://127.0.0.1:8000/docs

## Run Tests

    python -m pytest -v

## Future Improvements

- Improved code-quality rules
- User authentication
- Database integration
- AI-powered code explanations
- Web-based dashboard

## Author

Built as a software engineering portfolio project.