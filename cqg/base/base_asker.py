class BaseAsker(object):
    def __init__(self, analyzer,
                 transfomer,
                 transducer,
                 ranker = lambda x: x
                ):
        self.analyzer = analyzer
        self.transfomer = transfomer
        self.transducer = transducer
        self.ranker = ranker

    def __call__(self, ann):
        ann = self.analyzer(ann)
        ann = self.transfomer(ann)
        ann = self.transducer(ann)
        ann = self.ranker(ann)
        return ann

