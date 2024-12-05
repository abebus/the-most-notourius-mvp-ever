from pydantic_settings import BaseSettings
import pathlib


class Settings(BaseSettings):
    """Project settings."""

    BASE_DIR: pathlib.Path = pathlib.Path(__file__).resolve().parent.parent
