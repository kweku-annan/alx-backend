#!/usr/bin/env python3
"""Implements the FIFO Caching Policy"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A Class the implements FIFO Caching Policy"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Assigns to cache_data the item value of key"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                first_item = next(iter(self.cache_data))
                del self.cache_data[first_item]
                print("DISCARD: {}".format(first_item))

    def get(self, key):
        """Returns the value of self.cached_data linked to key"""
        return self.cache_data.get(key)
