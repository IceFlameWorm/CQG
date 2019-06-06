from .analyze import chinese_cut_sent
from .transform import SimpleTransformer


class BaseAsker(object):
    def __init__(self):
        pass

    def __call__(self, para):
        raise NotImplementedError


class SimpleAsker(BaseAsker):
    def __init__(self,
                 stanford_model
                ):
        self.tranformer = SimpleTransformer(stanford_model)

    def close(self):
        self.tranformer.close()


    def __call__(self, para):
        """
        1. 分句 -> 句子列表
        2. transform产生可用于生成问题地候选句子
            (1) 筛选不符合要求的句子
            (2) 句子简化
        3. transducer用候选句子产生问句
        4. ranker对产生的问题进行排序
        """

        ## 分句
        source_sens = self.get_sentences(para)

        ## 产生候选句子
        derived_sens = self.tranformer(source_sens)

        ## 产生问句

        ## 后处理

        ## 排序

    def get_sentences(self, para):
        """
        Args:
            para: str
        Returns:
            list[str]: list of sentences
        """
        sentences = chinese_cut_sent(para)
        return sentences



if __name__ == "__main__":
    para = "中国日前发表《关于中美经贸磋商的中方立场》白皮书，以权威而翔实的数据与事实，完整准确还原了中美经贸磋商的过程。国际社会由此进一步认清美国出尔反尔、违背共识、不讲诚信的真相，但美方对此坐不住了。6月3日，美国中国日前发表《关于中美经贸磋商的中方立场》白皮书，以权威而翔实的数据与事实，完整准确还原了中美经贸磋商的过程。国际社会由此进一步认清美国出尔反尔、违背共识、不讲诚信的真相，但美方对此坐不住了。6月3日，美国贸易代表办公室和财政部就中方立场白皮书发表声明，污称中国“玩推卸责任的游戏”“歪曲两国贸易谈判的性质和历史”。声明的字里行间，又进一步暴露了美方一贯歪曲事实、倒打一耙的真实面目。贸易代表办公室和财政部就中方立场白皮书发表声明，污称中国“玩推卸责任的游戏”“歪曲两国贸易谈判的性质和历史”。声明的字里行间，又进一步暴露了美方一贯歪曲事实、倒打一耙的真实面目。"
    import os
    stanford_model = os.path.join(os.environ["HOME"], 'model_files/stanfordcorenlp/stanford-corenlp-full-2018-02-27')
    asker = SimpleAsker(stanford_model)
    asker(para)
