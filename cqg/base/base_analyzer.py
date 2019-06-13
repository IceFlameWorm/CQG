class BaseAnalyzer(object):
    def __init__(self):
        pass

    def __call__(self, ann):
        text = ann.text
        ares = self.analyze(text)
        ann.ares = ares
        return ann

    def analyze(self, text):
        """
        对文本进行词法和语法分析，返回一个包含Sen对象的列表
        """
        raise NotImplementedError
