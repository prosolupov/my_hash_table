from typing import Any, Optional

from src.item import Item
from src.chain_item import ChainItem


class HashTable:
    def __init__(self):
        self.list_bucket: list = [None] * 8
        self.chain: ChainItem = ChainItem()

    def __get_id(self, key) -> int:
        return hash(key) % len(self.list_bucket)

    def __create_bucket(self, key, value) -> Item:
        return Item(hash(key), value)

    def __create_chain(self, id: int, bucket: Item):
        if type(self.list_bucket[id]) == Item:
            self.chain.add_bucket(self.list_bucket[id])
            self.chain.add_bucket(bucket)
            self.list_bucket[id] = self.chain
        else:
            self.chain.add_bucket(bucket)
            self.list_bucket[id] = self.chain

    def put(self, key, value):
        id = self.__get_id(key)
        bucket = self.__create_bucket(key, value)
        if self.list_bucket[id] is None:
            self.list_bucket[id] = bucket
        else:
            self.__create_chain(id, bucket)

    def get(self, key) -> Item:
        id = self.__get_id(key)
        if type(self.list_bucket[id]) is ChainItem:
            return self.chain.get_bucket(key)
        return self.list_bucket[id]

    def remove(self, key):
        id = self.__get_id(key)
        if type(self.list_bucket[id]) is ChainItem:
            self.chain.remove_link(key)
        else:
            self.list_bucket[id] = None

    def get_all(self):
        return self.list_bucket
