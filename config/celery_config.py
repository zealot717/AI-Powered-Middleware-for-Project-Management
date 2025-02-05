from celery import Celery

celery = Celery(
    "aerospace_ai",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)
