# QA API Automation Portfolio

A Python-based API automation testing project created to practice and demonstrate practical software quality engineering skills.

This project uses Python `requests` to send REST API requests and `pytest` to design and execute automated API tests.

The current test target is [JSONPlaceholder](https://jsonplaceholder.typicode.com/), a public REST API commonly used for testing and prototyping.

## Features

- REST API testing with Python
- GET, POST, and PUT request testing
- Positive and negative test scenarios
- HTTP status code validation
- JSON response validation
- Data-driven testing with `pytest.mark.parametrize`
- External JSON test data
- Reusable JSON test data loader
- Separation of API request logic, test data, and test assertions

## Tech Stack

- Python
- requests
- pytest
- JSON
- Git
- GitHub

## Project Structure

```text
qa-api-automation-portfolio/
├── tests/
│   ├── data/
│   │   └── user_cases.json
│   ├── utils/
│   │   ├── __init__.py
│   │   └── data_loader.py
│   ├── test_post.py
│   └── test_users.py
├── api_client.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Test Coverage

### Users API

Current tests cover:

- Getting an existing user
- Validating HTTP `200 OK` responses
- Validating user ID, name, and email fields
- Running the same test with multiple users using parameterization
- Loading test data from an external JSON file
- Getting a non-existing user
- Validating HTTP `404 Not Found` responses

### Posts API

Current tests cover:

- Getting an existing post
- Creating a new post with `POST`
- Updating an existing post with `PUT`
- Validating HTTP status codes
- Validating returned JSON payloads
- Comparing request data with response data

## Installation

Clone the repository:

```bash
git clone https://github.com/Fiona-Young-Code/qa-api-automation-portfolio.git
cd qa-api-automation-portfolio
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment on macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running Tests

Run all tests:

```bash
python -m pytest -v
```

Run tests and display `print()` output:

```bash
python -m pytest -v -s
```

## What I Practiced

Through this project, I practiced Python programming in the context of software testing.

Python concepts practiced include:

- Functions
- Parameters
- Return values
- Lists
- Dictionaries
- Tuples
- Imports and modules
- File reading
- JSON processing
- Assertions

API testing concepts practiced include:

- HTTP methods
- HTTP status codes
- Request payloads
- JSON responses
- Positive testing
- Negative testing
- Response validation
- Data-driven testing
- Parameterized testing
- Reusable test utilities

## Background

I created this project to strengthen my Python programming and API automation testing skills while building on my previous experience in software quality engineering.

The goal is to build a small but maintainable API testing framework that demonstrates practical testing and programming skills.

## Future Improvements

- Add DELETE request testing
- Add PATCH request testing
- Add more negative test cases
- Add boundary test cases
- Add HTML test reports
- Add GitHub Actions CI
- Add logging
- Add error handling
- Improve test data management