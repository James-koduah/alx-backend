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
        """put an item into the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get an item from cache"""
        if key is None:
            return None
        return self.cache_data.get(key)
