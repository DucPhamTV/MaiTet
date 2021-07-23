from io import StringIO

from lxml import etree


class LxmlParser:
    def __init__(self, html):
        self.html = html

    @staticmethod
    def xpath(html, xpath):
        parser = etree.HTMLParser()
        tree = etree.parse(StringIO(html), parser)
        result = tree.xpath(xpath)

        return result
