BOT_NAME = "cian"

SPIDER_MODULES = ["cian.spiders"]
NEWSPIDER_MODULE = "cian.spiders"


USER_AGENT = (
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0"
)

ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 1

DOWNLOAD_DELAY = 3

COOKIES_ENABLED = False

TELNETCONSOLE_ENABLED = False

DEFAULT_REQUEST_HEADERS = {
    "Host": "www.cian.ru",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "content-type": "application/json",
    "Origin": "https://www.cian.ru",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://www.cian.ru/",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-site",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "TE": "trailers",
}

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# ASYNCIO_EVENT_LOOP = "uvloop.Loop"

DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
    "scrapy.downloadermiddlewares.retry.RetryMiddleware": None,
    "cian.middlewares.fake_useragent.RandomUserAgentMiddleware": 400,
    "cian.middlewares.fake_useragent.RetryUserAgentMiddleware": 401
}

DOWNLOAD_HANDLERS = {
    "http": "scrapy_impersonate.ImpersonateDownloadHandler",
    "https": "scrapy_impersonate.ImpersonateDownloadHandler",
}

RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 429, 403, 400]

FAKE_USERAGENT_PROVIDER_PATH = "cian.middlewares.fake_useragent.providers.FakeChromePCProvider"

RETRY_TIMES = 20
