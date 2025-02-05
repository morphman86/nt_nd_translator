import json
import os
import time

class CacheManager:
    def __init__(self, cache_file="cache.json", cache_expiration=604800):
        """
        Initializes the CacheManager class.
        
        :param cache_file: The file to store the cache (default is "cache.json").
        :param cache_expiration: Cache expiration time in seconds (default is one week, 604800 seconds).
        """
        self.cache_file = cache_file
        self.cache_expiration = cache_expiration  # Default to 1 week
        self.cache = {}
        self.load_cache()

    def check_cache(self, phrase):
        """
        Check if the phrase exists in the cache and whether it's still valid.
        
        :param phrase: The phrase to check in the cache.
        :return: The translation if found and valid, otherwise None.
        """
        current_time = time.time()

        # Check for matching phrases in cache
        for cached_phrase, cached_entry in self.cache.items():
            # Check if the cache entry is still valid
            if current_time - cached_entry['timestamp'] <= self.cache_expiration:
                # If the phrase matches the cached entry, return the translation
                if cached_phrase == phrase:
                    return cached_entry['translation']
                # If the phrase is the translation of a cached phrase, return the original phrase
                elif cached_entry['translation'] == phrase:
                    return cached_phrase

        # Cache miss, return None if no matching translation is found
        return None

    def store_cache(self, phrase, translation):
        """
        Store a phrase and its translation in the cache.
        
        :param phrase: The phrase to store in the cache.
        :param translation: The corresponding translation to store.
        """
        self.cache[phrase] = {
            'translation': translation,
            'timestamp': time.time()
        }
        self.save_cache()

    def trim_cache(self):
        """
        Trim the cache to remove expired or unnecessary entries.
        This can be done periodically based on the expiration time.
        """
        current_time = time.time()
        phrases_to_remove = [
            phrase for phrase, entry in self.cache.items()
            if current_time - entry['timestamp'] > self.cache_expiration
        ]
        
        for phrase in phrases_to_remove:
            self.remove_cache_entry(phrase)

        self.save_cache()

    def remove_cache_entry(self, phrase):
        """
        Removes a specific entry from the cache.
        
        :param phrase: The phrase to remove from the cache.
        """
        if phrase in self.cache:
            del self.cache[phrase]

    def load_cache(self):
        """
        Load the cache from a persistent storage (file).
        """
        if os.path.exists(self.cache_file):
            with open(self.cache_file, 'r') as file:
                try:
                    self.cache = json.load(file)
                except json.JSONDecodeError:
                    self.cache = {}  # If file is corrupted, reset cache

    def save_cache(self):
        """
        Save the current state of the cache to persistent storage (file).
        """
        with open(self.cache_file, 'w') as file:
            json.dump(self.cache, file)

    def get_cache_size(self):
        """
        Returns the number of items in the cache.
        
        :return: The size of the cache.
        """
        return len(self.cache)
