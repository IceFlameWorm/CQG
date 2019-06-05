class BaseAsker(object):
    def __init__(self):
        pass

    def __call__(self, doc):
        raise NotImplementedError


class SimpleAsker(BaseAsker):
    def __init__(self):
        pass

    def __call__(self, doc):
        """
        1. 分句 -> 句子列表
        2. 对所有地句子进行句法解析 -> 解析树列表
        3. transform产生可用于生成问题地候选句子
            (1) 筛选不符合要求的句子
            (2) 句子简化
        4. transducer用候选句子产生问句
        5. ranker对产生的问题进行排序
        """

        ## 分句
        pass
