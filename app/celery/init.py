from celery import Celery
from celery.schedules import crontab

# from app.celery.tasks import choose_random_winner_with_chance
from settings import REDIS, RABBITMQ


celery_app = Celery(
    __name__,
    backend=REDIS,
    broker=RABBITMQ
)


celery_app.conf.beat_schedule = {
    'add-everyday-12-hour-30-minute': {
        'task': 'app.celery.tasks.choose_random_winner_with_chance',
        'schedule': crontab(hour=19, minute=25)
    },
}

celery_app.autodiscover_tasks(['app.celery.tasks'], force=True)
