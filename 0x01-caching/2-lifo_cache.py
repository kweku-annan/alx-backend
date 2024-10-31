#!/usr/bin/env python3
"""Holds the class LIFOCache"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Implements the LIFO caching policy"""

    def __init__(self):
        super().__init__()
        self.keys_list = []

    def put(self, key, item):
        """Assign to cache_data the item value for key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.keys_list.append(key)
        if len(self.cache_data) > self.MAX_ITEMS:
            last_key = self.keys_list[-2]
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))
            self.keys_list.pop(-2)

    def get(self, key):
        """Returns the value in self.cache_data linked to key"""
        return self.cache_data.get(key)
