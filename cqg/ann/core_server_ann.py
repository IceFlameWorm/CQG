from .base_ann import BaseAnn


class CoreServerAnn(BaseAnn):

    @property
    def source_sens(self):
        return self._source_sens

    @source_sens.setter
    def source_sens(self, sens):
        self._source_sens = sens

    @property
    def derived_sens(self):
        return self._derived_sens

    @derived_sens.setter
    def derived_sens(self, sens):
        self._derived_sens = sens

    @property
    def quests(self):
        return self._quests

    @quests.setter
    def quests(self, quests):
        self._quests = quests