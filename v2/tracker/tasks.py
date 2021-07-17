from core.celery import app
from v2.tracker.models import Tracker
from v2.crawlers.factory import Factory
from v2.parsers.lxml_parser import LxmlParser


@app.task
def crawl(tracker_id):
    print(f"Start crawling with {tracker_id}")
    tracker = Tracker.objects.get(uuid=tracker_id)
    print(f"Tracker info: {tracker}")
    crawler = Factory.create_crawler(tracker.url)
    response = crawler.run()
    result = LxmlParser.xpath(response.text, tracker.target)
    print(f"Crawl result: {result}")
