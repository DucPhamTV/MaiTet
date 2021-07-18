from core.celery import app
from v2.tracker.models import Tracker
from v2.crawlers.factory import Factory
from v2.parsers.lxml_parser import LxmlParser
from v2.results.models import Result


@app.task
def crawl(tracker_id):
    print(f"Start crawling with {tracker_id}")
    tracker = Tracker.objects.get(uuid=tracker_id)
    print(f"Tracker info: {tracker}")
    tracker.status = "ACTIVE"
    tracker.save()
    crawler = Factory.create_crawler(tracker.url)
    response = crawler.run()
    output = LxmlParser.xpath(response.text, tracker.target)
    print(f"Crawl result: {output}")
    tracker.status = "DONE"
    tracker.save()
    res = Result(tracker=tracker, value=output)
    res.save()
    print(f"Saved {res}")
