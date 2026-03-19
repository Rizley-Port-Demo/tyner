from fastapi import FastAPI
from .routers import health, items
app = FastAPI(title="My FastAPI App")
app.include_router(health.router)
app.include_router(items.router, prefix="/items")
