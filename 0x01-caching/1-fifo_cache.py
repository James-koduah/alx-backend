#!/usr/bin/env python3
"""
A Caching system using the FIFO method
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A Caching class using the FIFO method"""
    FIFO = []

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Put an item into the cache"""
        if len(
                self.cache_data
                ) >= self.MAX_ITEMS and key not in self.cache_data:
            delete_key = self.FIFO.pop(0)
            self.cache_data.pop(delete_key)
            print(f"DISCARD: {delete_key}")

        if key is not None and item is not None:
            self.cache_data[key] = item
            self.FIFO.append(key)

    def get(self, key):
        return self.cache_data.get(key)
