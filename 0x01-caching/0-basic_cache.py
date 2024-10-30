#!/usr/bin/env python3
"""Holds the BasicCache Class"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Implements Basic Caching"""

    def put(self, key, item):
        """Assign item value for key to cache_data"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Returns a value in cache_data"""
        return self.cache_data.get(key)
