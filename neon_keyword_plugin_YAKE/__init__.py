# # NEON AI (TM) SOFTWARE, Software Development Kit & Application Development System
# # All trademark and other rights reserved by their respective owners
# # Copyright 2008-2021 Neongecko.com Inc.
import yake
from ovos_plugin_manager.keywords import KeywordExtractor


class YAKEExtractor(KeywordExtractor):

    def __init__(self, config=None):
        super(YAKEExtractor, self).__init__(config)
        self.max_ngram_size = self.config.get("max_ngram_size", 2)

    def extract(self, text, lang):
        # extract keywords
        rake = yake.KeywordExtractor(n=self.max_ngram_size, lan=lang)
        keywords = rake.extract_keywords(text)
        # normalize scores
        scores = {k[0]: 1 - k[1] for k in keywords}
        return scores
