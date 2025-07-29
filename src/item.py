from dataclasses import dataclass
from typing import Any


class Item:
    def __init__(self, hash_object: int, value: Any):
        self.hash_object = hash_object
        self.value = value
        self.next = None