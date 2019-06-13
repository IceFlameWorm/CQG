from .base_transducer import BaseTransducer
from ..ann.core_server_quest import CoreServerQuest


class CoreServerTransducer(BaseTransducer):
    def __init__(self, entity2quest):
        self.entity2quest = entity2quest

    def transduce(self, derived_sens):
        quests = []
        for sen in derived_sens:
            qs = self._sen2quests(sen)
            quests += qs
        return quests

    def _sen2quests(self, sen):
        entitymentions = sen.entitymentions
        sen_text = sen.text
        quests = []
        for em in entitymentions:
            ner = em['ner']
            cb, ce = em['characterOffsetBegin'], em['characterOffsetEnd']
            if ner in self.entity2quest:
                quest = sen_text[:cb] + self.entity2quest[ner] + sen_text[ce:]
                quests.append(CoreServerQuest(quest, sen))
        return quests
