from core.celery import app
from v2.tracker.models import Tracker


@app.task
def crawl(tracker_id):
    print(f"start crawling with {tracker_id}")
    tracker = Tracker.objects.get(uuid=tracker_id)
    print(f"Tracker info: {tracker}")
