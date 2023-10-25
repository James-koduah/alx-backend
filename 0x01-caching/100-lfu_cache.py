#!/usr/bin/env python3
"""
A Caching system that implements the LFU algorithm
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """A Caching class using the LRU method
    if there is more that one item to remove we use the LRU method
    """

    LRU = []  # The latest key to be accessed is at the front of the queue
    frequency = {}  # Stores the frequency each key has been visited

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache"""
        cache_len = len(self.cache_data)
        if cache_len >= self.MAX_ITEMS and key not in self.cache_data:
            # list of all frequencies
            freq = [v for k, v in self.frequency.items()]
            least_freq = min(freq)
            """As we have lowest frequeny number
            we search through the LRU  to find a match for it and return the
            first match of the frequencies
            """
            delete_key = [
                    x for x in self.LRU if self.frequency[x] == least_freq][0]
            self.LRU.remove(delete_key)
            self.cache_data.pop(delete_key)
            self.frequency.pop(delete_key)
            print(f"DISCARD: {delete_key}")

        if key is not None and item is not None:
            """Cache format:
                self.cache_data = {
                "A": ["data", <frequency>],
                "B": ["data", 2],
                "C": ["data", 9]
                }
            """
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
                self.LRU.remove(key)
                self.LRU.append(key)
            else:
                self.cache_data[key] = item
                self.frequency[key] = 1
                self.LRU.append(key)

    def get(self, key):
        """Get value from cache"""
        value = self.cache_data.get(key)
        if value:
            self.LRU.remove(key)
            self.LRU.append(key)
            self.frequency[key] += 1
            return value
        return None
