class BaseTransformer(object):
    def __init__(self):
        pass

    def __call__(self, ann):
        source_sens = ann.source_sens
        derived_sens = self.tranform(source_sens)
        ann.derived_sens = derived_sens
        return ann

    def tranform(self, source_sens):
        raise NotImplementedError
