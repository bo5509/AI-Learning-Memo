### Why Tensorflow
* 社区的活跃度。在关注度、用户数上占有绝对优势。具体数字可以参照下图

|框架 |机构 |支持语言 |Stars |Forks |Contributors |
|--- |--- |--- |--- |--- |--- |
|TensorFlow |Google |Python、C++、Go |41628 |19339 |568 |
|Caffe |BVLC |Python、C++ |14956 |9282 |221 |
|Keras|fchollet|Python|10727|3575|322|
|CNTK|MS|C++|9063|2144|100|
|MXNet|DMLC|Python、C++、R|7393|2745|241|
|Torch7|Facebook|Lua|6111|1784|113|
|Theano|U-Montreal|Python|5352|1868|271|

* Google在业绩的号召力很强。强大的人工智能研发水平得到业界的广泛认可，所以大家对Google的框架充满信心

* 产品的迭代进化。每周都会有1M行以上的代码更新，多则数万行。产品本身优异的质量、快速的迭代更新、活跃的社区和积极的反馈，形成了良好的循环

* 各大框架都是支持Python的，目前在科学计算和数据挖掘领域可以说是独领风骚

* Python的各种库很完善。Web开发、数据可视化、数据预处理、数据库爬虫、爬虫等

* 主流框架的评分状况

|    |模型接口|接口|部署|性能|架构设计|总体评分|
|---|---|---|---|---|---|---|
|TensorFlow|80|80|90|90|100|88|
|Caffe|60|60|90|80|70|72|
|CNTK|50|50|70|100|60|66|
|Theano|80|70|40|50|50|58|
|Torch|90|70|60|70|90|76|
|MXNet|70|100|80|80|90|84|

* tensorFlow有强大的可视化组件：tensorboard

* tensorflow除了支持常见的网络结构（卷积神经网络、循环神经网络）外，还支持深度学习乃至其他计算密集的科学计算。

* TensorFlow可以方便的将训练好的模型方便的部署到多种硬件、操作平台上

* Google在2016年2月份开源TensorFlow Serving，这个组件可以将TensorFlow训练好的模型导出并部署到可以对外提供预测服务的Restful接口

[TensorFlow Serving架构](https://www.packtpub.com/graphics/9781786468574/graphics/image_06_002.jpg)

* Google的另一大利器就是Tensorboard各种可视化。标量、图片、音频、直方图、计算图。Events Dashboard还可以持续监控运行时的关键指标。loss、学习速率、准确率等

