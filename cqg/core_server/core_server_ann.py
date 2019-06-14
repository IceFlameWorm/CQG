from ..base.base_ann import BaseAnn
from .core_server_sen import CoreServerSen


class CoreServerAnn(BaseAnn):

    @property
    def source_sens(self):
        if not hasattr(self, "_source_sens"):
            ares = self.ares
            sens = ares["sentences"]
            self._source_sens = [CoreServerSen(sen_dict, self) for sen_dict in sens]

        return self._source_sens

    # @source_sens.setter
    # def source_sens(self, sens):
    #     self._source_sens = sens

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
