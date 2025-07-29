from typing import Any, Optional

from src.item import Item
from src.chain_item import ChainItem


class HashTable:
    def __init__(self):
        self.list_item: list = [None] * 8
        self.chain: ChainItem = ChainItem()

    def __get_id(self, key) -> int:
        return hash(key) % len(self.list_item)

    def __create_item(self, key, value) -> Item:
        return Item(hash(key), value)

    def __create_chain(self, id: int, bucket: Item):
        if type(self.list_item[id]) == Item:
            self.chain.add_item(self.list_item[id])
            self.chain.add_item(bucket)
            self.list_item[id] = self.chain
        else:
            self.chain.add_item(bucket)
            self.list_item[id] = self.chain

    def put(self, key, value):
        id = self.__get_id(key)
        item = self.__create_item(key, value)
        if self.list_item[id] is None:
            self.list_item[id] = item
        else:
            self.__create_chain(id, item)

    def get(self, key) -> Item:
        id = self.__get_id(key)
        if type(self.list_item[id]) is ChainItem:
            return self.chain.get_item(key)
        return self.list_item[id]

    def remove(self, key):
        id = self.__get_id(key)
        if type(self.list_item[id]) is ChainItem:
            self.chain.remove_link(key)
        else:
            self.list_item[id] = None

    def get_all(self):
        return self.list_item
