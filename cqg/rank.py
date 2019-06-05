class RankResult(object):
    def __init__(self, questions, scores):
        self.questions = questions
        self.scores = scores

    def topK(self, k):
        pass


class BaseRanker(object):
    def __init__(self):
        pass

    def __call__(self, questions):
        raise NotImplementedError


def SimpleRanker(BaseRanker):
    def __init__(self):
        pass

    def __call__(self, questions):
        scores = [0] * len(questions)
        res = RankResult(questions, scores)
        return res
