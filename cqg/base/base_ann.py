class BaseAnn(object):
    def __init__(self, text, comefrom = None):
        self._text = text
        self.comefrom = comefrom
        self._ancestors = self._get_ancesotrs()

    def _get_ancesotrs(self):
        ancestors = []
        anc = self.comefrom
        while anc is not None:
            ancestors.append(anc)
            anc = anc.comefrom
        return ancestors

    @property
    def ancestor_num(self):
        return len(self._ancestors)

    @property
    def text(self):
        return self._text

    @property
    def ares(self):
        return self._ares

    @ares.setter
    def ares(self, ares):
        self._ares = ares

    def get_ancestor(self, level = 1):
        assert 1 <= level <= self.ancestor_num, "level必须在[1, %d]区间内" % self.ancestor_num
        return self._ancestors[level - 1]
