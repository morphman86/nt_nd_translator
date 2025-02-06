import json
import os
import time

class CacheManager:
    def __init__(self, cache_file="cache.json", cache_expiration=604800):
        self.cache_file = cache_file
        self.cache_expiration = cache_expiration
        self.cache = self.load_cache()

    def check_cache(self, phrase):
        current_time = time.time()
        for cached_phrase, entry in self.cache.items():
            if current_time - entry['timestamp'] <= self.cache_expiration:
                if cached_phrase == phrase or entry['translation'] == phrase:
                    return cached_phrase if cached_phrase != phrase else entry['translation']
        return None

    def store_cache(self, phrase, translation):
        self.cache[phrase] = {'translation': translation, 'timestamp': time.time()}
        self.save_cache()

    def trim_cache(self):
        current_time = time.time()
        expired_phrases = [phrase for phrase, entry in self.cache.items() if current_time - entry['timestamp'] > self.cache_expiration]
        for phrase in expired_phrases:
            del self.cache[phrase]
        self.save_cache()

    def load_cache(self):
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                pass
        return {}

    def save_cache(self):
        with open(self.cache_file, 'w') as file:
            json.dump(self.cache, file)

    def get_cache_size(self):
        return len(self.cache)
