""" Usage:
    MaiTet$ PYTHONPATH=. python v2/crawlers/smoke_test/test_simple_crawler.py "https://hoayeuthuong.com/cua-hang-hoa/hoa-khuyen-mai/10708_you-are-beautiful" "/html/body/form/div[4]/div[3]/div/div[1]/div[1]/div/div[1]/div[2]/div[1]/h6[2]/span"
"""

import sys

from v2.crawlers.factory import Factory
from v2.parsers.lxml_parser import LxmlParser

url, target = sys.argv[1:3]
print(url, target)

crawler = Factory.create_crawler(url)
response = crawler.run()
result = LxmlParser.xpath(response.text, target)

print(f"Crawl result: {result[0].text}")
