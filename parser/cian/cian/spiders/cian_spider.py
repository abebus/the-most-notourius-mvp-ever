from __future__ import annotations

from typing import TYPE_CHECKING

import chompjs
import orjson
import scrapy

from ..items import ResultedFlat

if TYPE_CHECKING:
    import scrapy.http


class CianSpider(scrapy.Spider):
    name = "cian_spider"
    start_urls = ["https://www.cian.ru/sale/flat/309615216/"]

    def parse(self, response: scrapy.http.TextResponse):
        # Extract JavaScript containing offer data
        js_with_data = response.xpath(
            "//script[contains(text(), \"window._cianConfig['frontend-offer-card']\")]/text()"
        ).get()

        if not js_with_data:
            self.logger.error("JavaScript data not found. Retrying...")
            yield response.request.replace(dont_filter=True)
            return

        # Locate the "offerData" portion in the script
        idx_with_data = js_with_data.find("offerData")
        if idx_with_data == -1:
            self.logger.error("'offerData' key not found in JavaScript. Retrying...")
            yield response.request.replace(dont_filter=True)
            return

        stripped = js_with_data[idx_with_data:]
        data = chompjs.parse_js_object(stripped, loader=orjson.loads)

        # Extract address details
        addresses = data["offer"]["geo"]["address"]
        addr_data = {"full": []}
        for address in addresses:
            addr_data["full"].append(address["fullName"])
            if address["type"] == "location":
                addr_data["city"] = address["fullName"]
            elif address["type"] == "street":
                addr_data["street"] = address["fullName"]

        # Map feature labels to keys
        key_mapping = {
            "Тип жилья": "housing_type",
            "Общая площадь": "total_area",
            "Жилая площадь": "living_area",
            "Площадь кухни": "kitchen_area",
            "Высота потолков": "ceiling_height",
            "Отделка": "finishing",
            "Тип дома": "building_type",
            "Год постройки": "construction_year",
            "Тип перекрытий": "floor_type",
            "Отопление": "heating_type",
            "Аварийность": "emergency_status",
            "Санузел": "bathroom",
            "Вид из окон": "window_view",
            "Ремонт": "renovation",
        }

        features_data = {}
        for feature_block in data["features"]:
            for feature in feature_block["features"]:
                label = feature["label"].strip()
                value = feature["value"]
                key = key_mapping.get(label) or (
                    "balcony" if "лоджия" in label or "балкон" in label else None
                )
                if key:
                    features_data[key] = value

        # Calculate minimum time on foot to the subway
        time_on_foot_to_subway = None
        for subway in data["offer"]["geo"].get("undergrounds", []):
            if subway.get("travelType") == "walk":
                travel_time = subway.get("travelTime")
                if travel_time is not None:
                    time_on_foot_to_subway = (
                        min(time_on_foot_to_subway, travel_time)
                        if time_on_foot_to_subway is not None
                        else travel_time
                    )

        # Yield the ResultedFlat item
        yield ResultedFlat(
            cian_id=data["offer"]["cianId"],
            city=addr_data.get("city"),
            street=addr_data.get("street"),
            lat=data["offer"]["geo"]["coordinates"]["lat"],
            lon=data["offer"]["geo"]["coordinates"]["lng"],
            price_sq=data["priceInfo"]["pricePerSquareValue"],
            area=data["offer"]["totalArea"],
            floor=data["offer"]["floorNumber"],
            kitchen_area=features_data.get("kitchen_area"),
            bathroom_type=features_data.get("bathroom"),
            balconies=features_data.get("balcony"),
            renovation=features_data.get("renovation"),
            is_apartment=data["offer"].get("isApartments"),
            rooms=data["offer"]["roomsCount"],
            ceiling_height=data["offer"]["building"].get("ceilingHeight"),
            house_floors=data["offer"]["building"]["floorsCount"],
            house_wall_type=data["offer"]["building"]["houseMaterialType"],
            lifts=data["offer"].get("passengerLiftsCount"),
            freight_lifts=data["offer"].get("cargoLiftsCount"),
            time_on_foot_to_subway=time_on_foot_to_subway,
            build_year=data["offer"]["building"].get("buildYear"),
        )
