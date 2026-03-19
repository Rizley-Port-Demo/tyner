# tyner
Scaffolded with **Fastapi** via GitHub Actions.
## Getting started
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```
## Running tests
```bash
pip install pytest httpx
pytest
```

## Docker

### Build & run manually

```bash
docker build -t fastapi-app .
docker run -p 8080:8080 --env-file .env fastapi-app
```

### Using Docker Compose

```bash
cp .env.example .env   # fill in your values first
docker compose up --build
```

The app will be available at <http://localhost:8080>.
