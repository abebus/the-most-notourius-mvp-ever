from fastapi import FastAPI
from dataclasses import dataclass, asdict
import joblib
import pandas as pd
import asyncio
from functools import partial
from typing import Any

import logging

logging.basicConfig()

app = FastAPI()


class Model:
    def __init__(self) -> None:
        self._model = joblib.load(".static/kazan_model_xgb.pkl")

    def _predict(self, data: "Flat") -> float:
        data_dict = {k: [v] for k, v in asdict(data).items()}
        X = pd.DataFrame.from_dict(data_dict)
        res = self._model.predict(X)
        return res

    async def predict(self, data) -> dict:
        return await asyncio.get_event_loop().run_in_executor(
            None, partial(self._predict, data=data)
        )


model = Model()


@dataclass(slots=True, frozen=True)
class Flat:
    cian_id: int
    city: str
    street: str | None | Any
    lat: float
    lon: float
    price_sq: float
    area: float | None | Any
    floor: int | None | Any
    kitchen_area: float | None | Any
    bathroom_type: str | None | Any
    balconies: int | None | Any
    renovation: float | None | Any
    is_apartment: bool | None | Any
    rooms: int | None | Any
    ceiling_height: float | None | Any
    house_floors: int | None | Any
    house_wall_type: str | None | Any
    lifts: int | None | Any
    freight_lifts: int | None | Any
    time_on_foot_to_subway: float | None | Any
    build_year: int | None | Any


@app.post("/")
async def predict(data: Flat):
    logging.info(data)
    return {"square_price": float(await model.predict(data))}
