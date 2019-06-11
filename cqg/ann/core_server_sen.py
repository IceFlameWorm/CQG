from .base_ann import BaseAnn


class CoreServerSen(BaseAnn):
    def __init__(self, sen_dict, comefrom = None):
        self.sen_dict = sen_dict 
        self.tokens = self._sen_dict["tokens"]
        self.words = self._get_words()
        self.entitymentions = self._get_entitymentions()
        text = self._get_text(self.tokens)
        super(CoreServerSen, self).__init__(text, comefrom)


    def __len__(self):
        return len(self.sen_dict['tokens'])
    
    def _get_text(self, tokens):
        return "".join(token["word"] for token in tokens)
    
    def _get_words(self, tokens):
        return [token["word"] for token in tokens]
    
    def _get_entitymentions(self):
        return self.sen_dict.get('entitymentions', [])
