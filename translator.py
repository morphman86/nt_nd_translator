class Translator:
    def __init__(self, cache_manager, chatgpt_query):
        self.cache_manager = cache_manager
        self.chatgpt_query = chatgpt_query

    def nt_to_nd(self, phrase: str) -> str:
        return self.chatgpt_query.get_translation(phrase, "NT->ND")

    def nd_to_nt(self, phrase: str) -> str:
        return self.chatgpt_query.get_translation(phrase, "ND->NT")
