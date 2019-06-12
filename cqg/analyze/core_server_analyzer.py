import requests
from .base_analyzer import BaseAnalyzer

class CoreServerAnalyzer(BaseAnalyzer):
    def __init__(self, url = "http://localhost:9000",
                 properties = None,
                 lang = "zh",
                 timeout = 60 # 以秒为单位
                ):
        self.url = url
        self.timeout = timeout
        self.lang = lang
        self.timeout = timeout
        if properties is None:
            properties = {"annotators": "tokenize,ssplit,pos,ner",
                          "ssplit.boundaryTokenRegex": "[.。]|[!?！？]",
                          "pipelineLanguage": self.lang,
                          "'ner.applyFineGrained": False
                         }
        self.properties = properties


    def analyze(self, text):
        resp = requests.post(self.url, data = text.encode("utf8"),
                             params = {"properties": str(self.properties)}
                            )
        return resp.json()
