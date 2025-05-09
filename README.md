# ai-cicd-demo

This project is a simple web application built with Flask, designed to demonstrate a CI/CD pipeline with AI integration. It includes basic functionality and is structured for easy setup of GitHub Actions or other CI/CD tools for automated tests and AI-based checks.

## Project Structure

```
ai-cicd-demo
├── src
│   ├── app.py
│   ├── templates
│   │   └── index.html
│   └── static
│       └── style.css
├── tests
│   ├── __init__.py
│   └── test_app.py
├── .github
│   └── workflows
│       └── main.yml
├── requirements.txt
├── requirements-dev.txt
├── Dockerfile
├── .gitignore
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ai-cicd-demo.git
   cd ai-cicd-demo
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python src/app.py
   ```

5. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Running Tests

To run the tests, ensure your virtual environment is activated and execute:

```bash
pytest
```

## CI/CD Integration

This project includes a GitHub Actions workflow defined in `.github/workflows/main.yml` that automates the testing and deployment process.

## License

This project is licensed under the MIT License. See the LICENSE file for details.