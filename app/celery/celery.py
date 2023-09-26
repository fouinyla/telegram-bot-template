from celery import Celery
from kombu import Queue

from app.settings import redis_settings


celery_app = Celery(
    __name__,
    backend=redis_settings.url,
    broker=redis_settings.url,
)
celery_app.conf.task_queues = (
    Queue("light", routing_key="light"),
    Queue("heavy", routing_key="heavy"),
)
celery_app.autodiscover_tasks(['bot.background_tasks'], force=True)
