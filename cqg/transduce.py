class TransduceResult(object):
    def __init__(self, derived_sen, questions):
        self.derived_sen = derived_sen
        self.questions = questions


class BaseTransducer(object):
    def __init__(self):
        pass

    def __call__(self, derived_sen):
        raise NotImplementedError


def SimpleTransducer(BaseTransducer):
    def __init__(self):
        pass

    def __call__(self, derived_sen):
        res = TransduceResult(derived_sen, [])
        return res

