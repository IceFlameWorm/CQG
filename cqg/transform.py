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

    def __call__(self, source):
        raise NotImplementedError


class SimpleTransformer(BaseTransformer):
    def __init__(self):
        pass

    def __call__(self, source):
        res = TransformResult(source, [])
        return res
