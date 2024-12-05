class ImpersonateMiddleware:
    def __init__(self, crawler) -> None:
        self.browser = crawler.settings.get("FAKE_USERAGENT_RANDOM_UA_TYPE")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        request.meta["impersonate"] = self.browser
