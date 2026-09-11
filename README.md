# Python Flask App

Simple Flask web application with a ready-made GitHub Actions CI/CD pipeline.

## Project Structure

```
.
├── app.py                     # Main Flask app
├── requirements.txt           # Dependencies
├── Dockerfile                 # Container build
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── tests/
│   └── test_app.py
└── .github/
    └── workflows/
        └── ci-cd.yml          # CI/CD pipeline
```

## Run Locally

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

App will be available at `http://localhost:8000`.

## Run Tests

```bash
pip install pytest pytest-cov
pytest -v
```

## Run with Docker

```bash
docker build -t python-flask-app .
docker run -p 8000:8000 python-flask-app
```

## API Endpoints

| Method | Route              | Description               |
|--------|---------------------|---------------------------|
| GET    | `/`                  | Homepage                  |
| GET    | `/api/health`        | Health check               |
| GET    | `/api/greet/<name>`  | Greeting example           |
| POST   | `/api/echo`          | Echoes back JSON body      |

## CI/CD Pipeline

On every push/PR to `main`:
1. Lint + run tests across Python 3.10 / 3.11 / 3.12
2. Build & push Docker image (needs `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` secrets)
3. Deploy step (customize in `.github/workflows/ci-cd.yml`)
