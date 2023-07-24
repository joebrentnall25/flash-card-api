"""Dataclass and database interactions for Card"""
from dataclasses import dataclass
from datetime import datetime

from config.enums import CardDifficultyEnum


@dataclass
class Card:
    """Class to hold card data"""

    card_id: str
    title: str
    difficulty: CardDifficultyEnum
    last_tested: datetime
    contents: str
    last_updated: datetime
    date_created: datetime

