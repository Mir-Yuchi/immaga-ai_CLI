import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent


@dataclass
class ParserConfig:
    IMAGGA_API_SECRET: str
    IMAGGA_API_KEY: str


def load_config(env_filepath: str) -> ParserConfig:
    load_dotenv(env_filepath)
    IMAGGA_API_KEY = os.getenv('IMAGGA_API_KEY')
    IMAGGA_API_SECRET = os.getenv('IMAGGA_API_SECRET')
    return ParserConfig(IMAGGA_API_SECRET, IMAGGA_API_KEY)
