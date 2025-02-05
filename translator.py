from cache_manager import CacheManager
from chatgpt_query import ChatGPTQuery

class Translator:
    def __init__(self, cache_manager: CacheManager, chatgpt_query: ChatGPTQuery):
        """
        Initializes the Translator class with dependencies for cache management and querying ChatGPT.
        
        :param cache_manager: An instance of the CacheManager to manage caching.
        :param chatgpt_query: An instance of the ChatGPTQuery class to query OpenAI's API.
        """
        self.cache_manager = cache_manager
        self.chatgpt_query = chatgpt_query

    def nt_to_nd(self, phrase: str) -> str:
        """
        Translates a Neurotypical (NT) phrase to a Neurodivergent (ND) phrase (e.g., autism-friendly).
        
        :param phrase: The NT phrase to translate.
        :return: The translated ND phrase.
        """
        return self.chatgpt_query.get_translation(phrase, "NT->ND")

    def nd_to_nt(self, phrase: str) -> str:
        """
        Translates a Neurodivergent (ND) phrase (e.g., autism-related) to a Neurotypical (NT) phrase.
        
        :param phrase: The ND phrase to translate.
        :return: The translated NT phrase.
        """
        return self.chatgpt_query.get_translation(phrase, "ND->NT")
