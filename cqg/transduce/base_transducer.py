class BaseTransducer(object):
    def __init__(self):
        pass

    def __call__(self, ann):
        derived_sens = ann.derived_sens
        quests = self.transduce(derived_sens)
        ann.quests = quests
        return ann

    def transduce(self, derived_sens):
        raise NotImplementedError
