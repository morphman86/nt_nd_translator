import openai
from cache_manager import CacheManager
import settings  # Import the settings file

class ChatGPTQuery:
    def __init__(self, cache_manager: CacheManager):
        """
        Initializes the ChatGPTQuery class.
        
        :param cache_manager: An instance of the CacheManager to use caching.
        """
        self.cache_manager = cache_manager
        openai.api_key = settings.OPENAI_API_KEY  # Get the API key from the settings file

    def query_chatgpt(self, phrase: str, context: str) -> str:
        """
        Sends a query to the ChatGPT API and returns the response.
        
        :param phrase: The phrase to be translated.
        :param context: The context for translation (e.g., "NT->ND" or "ND->NT").
        :return: The translated phrase.
        """
        try:
            response = openai.Completion.create(
                engine=settings.OPENAI_ENGINE,  # Use engine from settings file
                prompt=self.pre_prompt(context, phrase),
                max_tokens=settings.MAX_TOKENS,  # Use max_tokens from settings file
                temperature=settings.TEMPERATURE,  # Use temperature from settings file
            )

            translated_text = response.choices[0].text.strip()
            return translated_text
        except openai.error.OpenAIError as e:
            print(f"Error while querying ChatGPT: {e}")
            return ""

    def pre_prompt(self, context: str, phrase: str) -> str:
        """
        Generates the appropriate prompt for ChatGPT based on the translation context.
        
        :param context: The translation context (either "NT->ND" or "ND->NT").
        :param phrase: The phrase to translate.
        :return: The generated prompt string for ChatGPT.
        """
        if context == "NT->ND":
            return f"Translate the following phrase into a way that someone with autism would easily understand: {phrase}"
        elif context == "ND->NT":
            return f"Translate the following phrase into a way that a neurotypical person would understand, assuming it is said by an autistic person: {phrase}"
        else:
            raise ValueError("Invalid context. Use 'NT->ND' or 'ND->NT'.")

    def get_translation(self, phrase: str, context: str) -> str:
        """
        Gets the translation of a phrase, first checking the cache and querying ChatGPT if necessary.
        
        :param phrase: The phrase to be translated.
        :param context: The context for translation (e.g., "NT->ND" or "ND->NT").
        :return: The translated phrase.
        """
        # Check the cache first
        cached_translation = self.cache_manager.check_cache(phrase)
        if cached_translation:
            print(f"Translation cached")
            return cached_translation

        # If not in the cache, query ChatGPT
        print(f"Translation not cached, getting from external service using context {context}")
        translation = self.query_chatgpt(phrase, context)

        # Store the translation in cache for future use
        if translation:
            self.cache_manager.store_cache(phrase, translation)

        return translation
