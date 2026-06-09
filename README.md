# DevOps Health App

A containerised Python Flask application with a full CI/CD pipeline using GitHub Actions and Docker Hub.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Application | Python 3.11, Flask |
| Containerisation | Docker, Docker Compose |
| CI/CD | GitHub Actions |
| Registry | Docker Hub |

## CI/CD Pipeline

Every push to `main` triggers the pipeline:

```
Push to main
     │
     ▼
┌─────────────┐
│  Run Tests  │  pytest — health endpoint, index page
└──────┬──────┘
       │ pass
       ▼
┌──────────────────┐
│  Build Docker    │  docker build
│  Image           │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│  Push to         │  :latest + :<git-sha>
│  Docker Hub      │
└──────────────────┘
```

## Run Locally

**With Docker Compose (recommended):**
```bash
docker compose up --build
```

**With Docker directly:**
```bash
docker build -t devops-health-app .
docker run -p 5000:5000 devops-health-app
```

**Without Docker:**
```bash
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000

## API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health dashboard UI |
| `/api/health` | GET | JSON health check |

**Sample response from `/api/health`:**
```json
{
  "status": "healthy",
  "hostname": "abc123",
  "python_version": "3.11.9",
  "environment": "production",
  "timestamp": "2026-06-09T11:00:00Z"
}
```

## Setup: GitHub Actions Secrets

Add the following secrets to your GitHub repo (Settings → Secrets → Actions):

| Secret | Value |
|--------|-------|
| `DOCKERHUB_USERNAME` | Your Docker Hub username |
| `DOCKERHUB_TOKEN` | Docker Hub access token (not your password) |

## Run Tests

```bash
pip install pytest
pytest tests/ -v
```
