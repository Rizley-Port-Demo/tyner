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
