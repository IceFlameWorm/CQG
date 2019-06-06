from stanfordcorenlp import StanfordCoreNLP

class TransformResult(object):
    def __init__(self, source, derived):
        self.source = source
        self.derived = derived


class BaseTransformer(object):
    """
    对输入的句子进行处理，产生候选的用于生成问题的陈述句
    """
    def __init__(self):
        pass

    def __call__(self, source_sens):
        raise NotImplementedError


class SimpleTransformer(BaseTransformer):
    def __init__(self, stanford_model,
                 max_len = 50,
                ):
        self.nlp = StanfordCoreNLP(stanford_model, lang = "zh")
        self.max_len = max_len

    def __call__(self, source_sens):
        ## 句子筛选
        kepted_sens = self.filter_sens(source_sens)
        # 句子简化
        res = None
        return res

    def close(self):
        self.nlp.close()

    def filter_sens(self, source_sens):
        kepted_sens = [sen for sen in source_sens if len(sen) <= self.max_len]
        return kepted_sens
