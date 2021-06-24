from core.celery import app


@app.task
def crawl(tracker_id, url, target):
    print(f"start crawling with {tracker_id}")
