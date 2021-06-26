from lxml import etree


class LxmlParser:
    def __init__(self, html):
        self.html = html

    @staticmethod
    def xpath(html, xpath):
        parser = etree.HTMLParser()
        tree = etree.parse(html, parser)
        result = tree.xpath(xpath)
        print(result)

        return result
