from ..base.base_transformer import BaseTransformer
from .core_server_analyzer import CoreServerAnalyzer
from .core_server_ann import CoreServerAnn
from .core_server_sen import CoreServerSen


class CoreServerTransformer(BaseTransformer):
    def __init__(self, max_len = None, by_punc = True, rule = None,
                 url = "http://localhost:9000/tregex", lang = 'zh',
                 timeout = 60, # 以秒为单位
                 post_min_len = None,
                 post_by_ner = False,
                 entity_labels = None
                ):
        self.max_len = max_len
        self.by_punc = by_punc
        self.puncs = ['?!？！']
        self.rule = rule
        self.lang = lang
        self.properties = {"pipelineLanguage": self.lang}
        self.url = url
        self.timeout = timeout
        self.analyzer = CoreServerAnalyzer()
        self.post_min_len = post_min_len
        self.post_by_ner = post_by_ner
        self.entity_labels = entity_labels

    def tranform(self, source_sens):
        kept_sens = self._filter(source_sens)
        simplified_sens = self._simplify(kept_sens)
        derived_sens = self._post_filter(simplified_sens)
        return derived_sens

    def _filter(self, source_sens):
        kept_sens = source_sens
        if self.max_len is not None:
            kept_sens = self._filter_by_len(kept_sens)
        if self.by_punc:
            kept_sens = self._filter_by_punc(kept_sens)
        return kept_sens

    def _filter_by_len(self, sens):
        kept_sens = [sen for sen in sens if len(sen) <= self.max_len]
        return kept_sens

    def _filter_by_punc(self, sens):
        kept_sens = [sen for sen in sens if sen.words[-1].strip() not in self.puncs]
        return kept_sens

    def _simplify(self, kept_sens):
        simplified_sens = []
        for sen in kept_sens:
            res = requests.post(self.url, data=sen.text.encode("utf8"), params = {"pattern": self.rule, "properties": str(self.properties)},
                                timeout = self.timeout
                               )
            res_dict = res.json()
            sub_sens = res_dict['sentences'][0]
            for sub_k, sub_v in sub_sens.items():
                    sub_treestr = sub_v["match"]
                    sub_text = self._treestr2text(sub_treestr)
                    tmp_ann = CoreServerAnn(sub_text)
                    tmp_ann = self.analyzer(tmp_ann)
                    tmp_sens = tmp_ann.ares["sentences"]
                    simplified_sens += [CoreServerSen(tmp_ann, sen) for tmp_sen in tmp_sens]
        return simplified_sens

    def _treestr2text(self, treestr):
        pattern = r'[^\(\s\)]+\)'
        words_ = re.findall(pattern, treestr)
        words = [w_[:-1] for w_ in words_]
        text = "".join(words)
        return text

    def _post_filter(self, simplified_sens):
        kept_sens = simplified_sens
        if self.post_min_len is not None:
            kept_sens = self._post_filter_by_len(kept_sens)
        if self.post_by_ner:
            kept_sens = self._post_filter_by_ner(kept_sens)
        return kept_sens

    def _post_filter_by_len(self, sens):
        kept_sens = [sen for sen in sens if len(sen) >= self.post_min_len]
        return kept_sens

    def _post_filter_by_ner(self, sens):
        def check_entity(sen):
            entitymentions = sen.entitymentions
            if entitymentions == []:
                return False

            if any(em['ner'] in self.entity_labels for em in entitymentions) == False:
                return False

            return True
        kept_sens = [sen for sen in sens if check_entity(sen)]
        return kept_sens
