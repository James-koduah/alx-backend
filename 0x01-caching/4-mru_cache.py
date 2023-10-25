#!/usr/bin/env python3
"""
A Caching system that implements the MRU method(Most Recently Used)
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A Caching class using the MRU method"""
    MRU = []

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """add an item to the cache"""
        cache_length = len(self.cache_data)
        if cache_length >= self.MAX_ITEMS and key not in self.cache_data:
            delete_key = self.MRU.pop()
            self.cache_data.pop(delete_key)
            print(f"DISCARD: {delete_key}")

        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.MRU:
                self.MRU.remove(key)
            self.MRU.append(key)

    def get(self, key):
        """Get value from cache"""
        value = self.cache_data.get(key)
        if value:
            self.MRU.remove(key)
            self.MRU.append(key)
        return value
