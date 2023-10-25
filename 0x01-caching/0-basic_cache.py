#!/usr/bin/env python3
"""
Implementing a basic caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A Basic caching system with no limit"""
    def __init__(self):
        super(BasicCache, self).__init__()

    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        if key is None:
            return None
        self.cache_data.get(key)
