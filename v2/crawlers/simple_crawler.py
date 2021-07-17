import requests


EXTRA_HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "cross-site",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "cookie": "usidtb=8sbET4wKz5gEXfpDlurZ6IE6Emiwe1Fj; ASP.NET_SessionId=x20reqk3w2vyj4d4mcylgnut; _ga=GA1.3.1559805767.1598054015; __zlcmid=znjNSkVpblt66d; _ym_uid=1600177858801107491; _ym_d=1600177858; SERVERID=B; __auc=780feb3f174b1275b10ad9f2e3f; tour-guide-ui-2020=1; ins-storage-version=20; _gid=GA1.3.2100659325.1624717681; _hjid=b166690d-5ee8-46fc-83a9-422a915401b3; _gcl_au=1.1.51779347.1624717683; __zi=3000.SSZzejyD6jy_Zl2jp1eKttQU_gxC3nMGTChWuC8NLincmF_oW0L0rscUzFZ5JaZHPPhyiS1BIvzcbVowma98bJ4.1; USER_PRODUCT_SEARCH=38%7C283%7CHP%7C36%7C317%7C361%7C0%2C30359944; __cf_bm=1ffa2cf50c21f5c1d432e07f9cefeeddef85b70d-1624775065-1800-AYCEjNO2ZCFXmPrpm6QsNjO8QaYZiKXxHErLQKv+aOGhmqCxWtQwnzdCWcRguDgjCiA4DuN92LbWNhYjDr3sKF8=; sidtb=VbVJ81zdaf0gHcrYDEj5OPiz8y96m48a; _gat_UA-3729099-1=1; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0; _hjIncludedInSessionSample=0"
}

EXTRA_HEADER_2 = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "cross-site",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "usidtb=8sbET4wKz5gEXfpDlurZ6IE6Emiwe1Fj; ASP.NET_SessionId=x20reqk3w2vyj4d4mcylgnut; _ga=GA1.3.1559805767.1598054015; __zlcmid=znjNSkVpblt66d; _ym_uid=1600177858801107491; _ym_d=1600177858; SERVERID=B; __auc=780feb3f174b1275b10ad9f2e3f; tour-guide-ui-2020=1; ins-storage-version=20; _gid=GA1.3.2100659325.1624717681; _hjid=b166690d-5ee8-46fc-83a9-422a915401b3; _gcl_au=1.1.51779347.1624717683; __zi=3000.SSZzejyD6jy_Zl2jp1eKttQU_gxC3nMGTChWuC8NLincmF_oW0L0rscUzFZ5JaZHPPhyiS1BIvzcbVowma98bJ4.1; USER_PRODUCT_SEARCH=38%7C283%7CHP%7C36%7C317%7C361%7C0%2C30359944; __cf_bm=1ffa2cf50c21f5c1d432e07f9cefeeddef85b70d-1624775065-1800-AYCEjNO2ZCFXmPrpm6QsNjO8QaYZiKXxHErLQKv+aOGhmqCxWtQwnzdCWcRguDgjCiA4DuN92LbWNhYjDr3sKF8=; sidtb=VbVJ81zdaf0gHcrYDEj5OPiz8y96m48a; _gat_UA-3729099-1=1; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0; _hjIncludedInSessionSample=0"
}

class SimpleCrawler:
    """Suitablle for website/url doesn't require browser render"""
    def __init__(self, url):
        self.url = url

    def run(self):
        # TODO: Implement caching
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(self.url, headers=EXTRA_HEADERS)
        #print(f"Response: {response.text}")
        response.raise_for_status()

        return response
