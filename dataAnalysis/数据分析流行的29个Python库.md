**01 Python标准库**

Python标准库提供了丰富的功能，包括文本/二进制数据处理、数学运算、函数式编程、文件/目录访问、数据持久化、数据压缩/归档、加密、操作系统服务、并发编程、进程间通信、网络协议、JSON / XML /其他Internet数据格式、多媒体、国际化、GUI、调试、分析等。下面列出了一部分Python标准库模块。



1. **collections：**建立在列表、元组、字典和集合基础上的加强版数据结构。
2. **csv：**处理用逗号分隔值的文件。
3. **datetime, time：**日期和时间操作。
4. **decimal：**定点或浮点运算，包括货币计算。
5. **doctest：**通过验证测试或嵌入在docstring中的预期结果进行简单的单元测试。
6. **json：**处理用于Web服务和NoSQL文档数据库的JSON（JavaScript Object Notation）数据。
7. **math：**常见的数学常量和运算。
8. **os：**与操作系统进行交互。
9. **queue：**一种先进先出的数据结构。
10. **random：**伪随机数操作。
11. **re：**用于模式匹配的正则表达式。
12. **sqlite3：**SQLite关系数据库访问。
13. **statistics：**数理统计函数，如均值、中值、众数和方差等。
14. **string：**字符串操作。
15. **sys：**—命令行参数处理，如标准输入流、输出流和错误流。
16. **timeit：**性能分析。



Python拥有一个庞大且仍在快速增长的开源社区，社区中的开发者来自许多不同的领域。该社区中有大量的开源库是Python受欢迎的最重要的原因之一。



许多任务只需要几行Python代码就可以完成，这会令人感到很神奇。下面列出了一些流行的数据科学库。



**02 科学计算与统计**



1. **NumPy**（Numerical Python）：Python没有内置的数组数据结构。它提供的列表类型虽然使用起来更方便，但是处理速度较慢。NumPy提供了高性能的ndarray数据结构来表示列表和矩阵，同时还提供了处理这些数据结构的操作。详细教程请戳👉[高能！8段代码演示Numpy数据运算的神操作](http://mp.weixin.qq.com/s?__biz=MzI5OTk5OTM2Mw==&mid=2247499023&idx=2&sn=3da2829fd018e024e1c5249025d1d901&chksm=ec8cb4e3dbfb3df5f3ce1bac556a50c4e738adfe12367d133f126d651e637f7664fe3afb2b8f&scene=21#wechat_redirect)
2. **SciPy**（Scientific Python）：SciPy基于NumPy开发，增加了用于科学处理的程序，例如积分、微分方程、额外的矩阵处理等。scipy.org负责管理SciPy和NumPy。详细教程请戳👉[3段极简代码带你入门Python科学计算库SciPy](http://mp.weixin.qq.com/s?__biz=MzI5OTk5OTM2Mw==&mid=2247526051&idx=3&sn=f0dcf1abfc48000922d53f307809cfe1&chksm=ec8c2f4fdbfba6596adf249991836651c44d01b080491b3c87cc1b2b914babaf12de779d786f&scene=21#wechat_redirect)
3. **StatsModels：**为统计模型评估、统计测试和统计数据研究提供支持。





**03 数据处理与分析**



1. **pandas：**一个非常流行的数据处理库。pandas充分利用了NumPy的ndarray类型，它的两个关键数据结构是Series（一维）和DataFrame（二维）。详细教程请戳👉[Pandas最详细教程来了！](http://mp.weixin.qq.com/s?__biz=MzI5OTk5OTM2Mw==&mid=2247526802&idx=2&sn=25b1def7cb58e8cab3c9cf1a7dc57dc4&chksm=ec8c207edbfba968f6b92eabd1c776cfdf1db0fc1e8db185f432f1d997883dd968b6d5c1fefc&scene=21#wechat_redirect)



**04 可视化**

1. **Matplotlib：**可高度定制的可视化和绘图库。Matplotlib可以绘制正规图、散点图、柱状图、等高线图、饼图、矢量场图、网格图、极坐标图、3D图以及添加文字说明等。详细教程请戳👉[Python实操：手把手教你用Matplotlib把数据画出来](http://mp.weixin.qq.com/s?__biz=MzI5OTk5OTM2Mw==&mid=2247499028&idx=2&sn=f9028aebf79f9d8f3ca15f81301dc270&chksm=ec8cb4f8dbfb3deef5f4970cf799e172d23a9475af707c6ee2d7eb013e2397815ad542565223&scene=21#wechat_redirect)
2. **Seaborn：**基于Matplotlib构建的更高级别的可视化库。与Matplotlib相比，Seaborn改进了外观，增加了可视化的方法，并且可以使用更少的代码创建可视化。详细教程请戳👉[数据可视化干货：使用pandas和seaborn制作炫酷图表（附代码）](http://mp.weixin.qq.com/s?__biz=MzI5OTk5OTM2Mw==&mid=2247499389&idx=2&sn=46e6408309e40901aa41169eb3b3262e&chksm=ec8cb791dbfb3e87a97bd5ac83908db59ea3f69e0d2c3588fc17a91016802767b4f98e960ca4&scene=21#wechat_redirect)



**05 机器学习、深度学习和强化学习**

1. **scikit-learn：**一个顶级的机器学习库。机器学习是AI的一个子集，深度学习则是机器学习的一个子集，专注于神经网络。
2. **Keras：**最易于使用的深度学习库之一。Keras运行在TensorFlow（谷歌）、CNTK（微软的深度学习认知工具包）或Theano（蒙特利尔大学）之上。
3. **TensorFlow：**由谷歌开发，是使用最广泛的深度学习库。TensorFlow与GPU（图形处理单元）或谷歌的定制TPU（Tensor处理单元）配合使用可以获得最佳的性能。TensorFlow在人工智能和大数据分析中有非常重要的地位，因为人工智能和大数据对数据处理的需求非常巨大。本书使用TensorFlow内置的Keras版本。详细教程请戳👉[TensorFlow是什么？怎么用？终于有人讲明白了](http://mp.weixin.qq.com/s?__biz=MzI5OTk5OTM2Mw==&mid=2247498807&idx=2&sn=7d19f5a8b15b1033ac4c8fbb887a9765&chksm=ec8cb5dbdbfb3ccd603444076b30d311dd572c3251fdfcc6f69d8c096719caa36c6047a442d6&scene=21#wechat_redirect)
4. **OpenAI Gym：**用于开发、测试和比较强化学习算法的库和开发环境。



**06 自然语言处理**



1. **NLTK**（Natural Language Toolkit）：用于完成自然语言处理（NLP）任务。
2. **TextBlob：**一个面向对象的NLP文本处理库，基于NLTK和模式NLP库构建，简化了许多NLP任务。
3. **Gensim：**功能与NLTK类似。通常用于为文档合集构建索引，然后确定另一个文档与索引中每个文档的相似程度。