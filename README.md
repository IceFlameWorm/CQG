# Chinese Question Generation

参考Michael Heilman Noah A. Smith等人的论文 Good Question! Statistical Ranking for Question Generation，和报告 Question generation via overgenerating transformations and ranking，尝试基于词法和语法分析的结果构建规则，从给定的中文文本中提取出可用于生成问题的句子，并为这些句子生成对应的问题。这么做的目的主要是为了熟悉NLP分析的各种功能以及基于规则的问题生成方法。

## 基本流程
作者提出的问题生成方法主要包含以下3步：
1. 陈述句提取 - 从给定文本中提取出陈述句，作者认为只有陈述句才会包含确定信息，才能用于生成问句
2. 问句生成 - 基于命名实体识别，词法和句法变换，将成陈述句转换成问句
3. 排序 - 对上述步骤生成的大量问题进行排序，筛选掉那些不适合的问句
具体算法请参见作者论文和报告。

## 目前进展
1. 目前只尝试实现了简化版本的陈述句提取和问句生成，排序这一步还没有做，感兴趣的可以看notebooks下的代码。
2. cqg目录下把流程各个部分进行了模块化，基本上于notebooks下的模块一致。初步对模块进行了完善和测试，不过仍然有不少hard code的地方，今后有时间再进一步改善。

## 后期规划
1. 尝试实现排序的功能
2. 功能模块化，放入cqg目录中

## 开发环境
1. python3.6
2. Stanford CoreNLP 3.9.2, 需要下载中文模型
3. java 12

## 代码运行提示
notebooks下的代码运行前需要提前运行Stanford CoreNLP Server，具体步骤参考Stanford CoreNLP文档


## 参考资料
- Good Question! Statistical Ranking for Question Generation，原文在doc目录下
- Question generation via overgenerating transformations and ranking，原文在doc目录下
- [QA system - Question Generation](http://www.shuang0420.com/2017/04/06/QA%20system%20-%20Question%20Generation/)
- [Stanford CoreNLP](https://stanfordnlp.github.io/CoreNLP/)
- [Tregex, Tsurgeon and Semgrex](https://nlp.stanford.edu/software/tregex.html)
