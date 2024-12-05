class ImpersonateMiddleware:
    def process_request(self, request, spider):
        request.cookies.extend(
            {
                "forever_region_id": "4777",
                "login_button_tooltip_key": "1",
                "session_main_town_region_id": "4777",
                "session_region_id": "4777",
            }
        )
