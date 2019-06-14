from ..base.base_asker import BaseAsker
from .core_server_analyzer import CoreServerAnalyzer
from .core_server_transformer import CoreServerTransformer
from .core_server_transducer import CoreServerTransducer


class CoreServerAsker(BaseAsker):
    def __init__(self):
        rule = "IP<(NP=np $..(VP=vp ?$.. PU)) >(ROOT|IP|CP)"
        entity2quest = {"LOCATION": "{ 哪里 | 什么地方 }",
                        "PERSON": "{ 谁 }",
                        "GPE": "{ 哪里 | 什么地方 }",
                        "ORGANIZATION": "{ 什么 组织|机构 }"
                       }
        entity_labels = list(entity2quest.keys())
        analyzer = CoreServerAnalyzer()
        transfomer = CoreServerTransformer(rule = rule,
                                           entity_labels = entity_labels,
                                           post_by_ner = True
                                          )
        transducer = CoreServerTransducer(entity2quest)
        super(CoreServerAsker, self).__init__(analyzer,
                                              transfomer,
                                              transducer)
