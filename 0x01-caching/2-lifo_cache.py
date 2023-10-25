#!/usr/bin/env python3
"""
A Caching system using the LIFO method
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A caching class using the LIFO method"""
    LIFO = []

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Put an item into the cache"""
        cache_length = len(self.cache_data)
        if cache_length >= self.MAX_ITEMS and key not in self.cache_data:
            delete_key = self.LIFO.pop()
            self.cache_data.pop(delete_key)
            print(f"DISCARD: {delete_key}")

        if key is not None and item is not None:
            self.cache_data[key] = item
            self.LIFO.append(key)

    def get(self, key):
        """Get value from cache"""
        return self.cache_data.get(key)
