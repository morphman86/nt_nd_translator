import openai
from cache_manager import CacheManager
import settings

class ChatGPTQuery:
    def __init__(self, cache_manager: CacheManager):
        self.cache_manager = cache_manager
        openai.api_key = settings.OPENAI_API_KEY

    def query_chatgpt(self, phrase: str, context: str) -> str:
        try:
            response = openai.Completion.create(
                engine=settings.OPENAI_ENGINE,
                prompt=self.pre_prompt(context, phrase),
                max_tokens=settings.MAX_TOKENS,
                temperature=settings.TEMPERATURE,
            )
            return response.choices[0].text.strip()
        except openai.error.OpenAIError as e:
            print(f"Error querying ChatGPT: {e}")
            return ""

    def pre_prompt(self, context: str, phrase: str) -> str:
        if context == "NT->ND":
            return f"Translate the following phrase into a version that someone with autism would understand. Avoid figurative language, metaphors, or idioms: {phrase}"
        elif context == "ND->NT":
            return f"Translate the following phrase into a version that a neurotypical person would understand, considering the communication style of an autistic person: {phrase}"
        else:
            raise ValueError("Invalid context. Use 'NT->ND' or 'ND->NT'.")

    def get_translation(self, phrase: str, context: str) -> str:
        cached_translation = self.cache_manager.check_cache(phrase)
        if cached_translation:
            print("Translation cached")
            return cached_translation

        print(f"Getting translation from service using context {context}")
        translation = self.query_chatgpt(phrase, context)
        if translation:
            self.cache_manager.store_cache(phrase, translation)
        return translation
