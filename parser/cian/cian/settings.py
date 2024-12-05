import logging
import sys

from loguru import logger

BOT_NAME = "cian"

SPIDER_MODULES = ["cian.spiders"]
NEWSPIDER_MODULE = "cian.spiders"


USER_AGENT = (
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0"
)

ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 1

DOWNLOAD_DELAY = 5

COOKIES_ENABLED = True

TELNETCONSOLE_ENABLED = False

DEFAULT_REQUEST_HEADERS = {
    "Host": "kazan.cian.ru",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "content-type": "application/json",
    "DNT": "1",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
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
    "cian.middlewares.impersonate.ImpersonateMiddleware": 1,
    "cian.middlewares.fake_useragent.RandomUserAgentMiddleware": 400,
    "cian.middlewares.fake_useragent.RetryUserAgentMiddleware": 401,
}

DOWNLOAD_HANDLERS = {
    "http": "scrapy_impersonate.ImpersonateDownloadHandler",
    "https": "scrapy_impersonate.ImpersonateDownloadHandler",
}

RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 429, 403, 400]
FAKEUSERAGENT_PROVIDERS = [
    # this is the first provider we'll try
    "cian.middlewares.fake_useragent.providers.FakeUserAgentProvider",
    # if FakeUserAgentProvider fails, we'll use faker to generate a user-agent string for us
    "cian.middlewares.fake_useragent.providers.FakerProvider",
    # fall src.to USER_AGENT value
    "cian.middlewares.fake_useragent.providers.FixedUserAgentProvider",
]
FAKE_USERAGENT_RANDOM_UA_TYPE = FAKER_RANDOM_UA_TYPE = "chrome"
FAKEUSERAGENT_FALLBACK = USER_AGENT
RANDOM_UA_PER_PROXY = True
RETRY_TIMES = 3

LOG_LEVEL = "DEBUG"
#
# LOG_FILE = "/logs/spider.log"


class InterceptHandler(logging.Handler):
    """
    Add logging handler to augment python stdlib logging.

    Logs which would otherwise go to stdlib logging are redirected through
    loguru.
    """

    @logger.catch(default=True, onerror=lambda _: sys.exit(1))
    def emit(self, record):
        # Get corresponding Loguru level if it exists.
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message.
        frame, depth = sys._getframe(6), 6
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)
