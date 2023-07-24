"""Dataclass and database interactions for Collection"""
from dataclasses import dataclass


@dataclass
class Collection:
    """Class to hold collection data"""

    collection_id: str
    name: str
    category: str
    description: str