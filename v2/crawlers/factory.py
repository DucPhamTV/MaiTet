from .simple_crawler import SimpleCrawler


class Factory:
    def __init__(self, url):
        self.url = url

    @staticmethod
    def create_crawler(url):
        # TODO: Analyse url
        # Hard code to return simple crawler
        return SimpleCrawler(url)
