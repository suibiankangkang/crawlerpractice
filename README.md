【暂时停更】

----------------------------------------------------------


爬虫超基础入门，菜鸡学习笔记，欢迎指点，大神轻喷

----------------------------------------------------------



001fiction.py

爬取小说，简单的静态爬虫代码，并将每章内容分别保存为txt文件

（可能会遇到304的问题，后面会再补充解决）

----------------------------------------------------------

002qiubai.py

爬取糗事百科内的笑话，简单的静态爬虫代码，并保存为txt文件

爬取1-13页（一共就13页）

爬取内容包括：作者、点赞数、文本内容

----------------------------------------------------------

003college_rank.py

爬取全国大学排名，简单的静态爬取代码，并保存为CSV文件

爬取内容包括：排名，大学名称，综合得分

----------------------------------------------------------

004wordcloud.py

爬取公开文件，简单的静态爬取代码，制作成词云后，保存为png文件

----------------------------------------------------------

005scrapy_test.zip

【其中有2个爬虫实例】example demo

要预先安装scrapy库，需解压

在cmd命令下运行： scrapy crawl example

简单抓取百度首页输入框的内容


在cmd命令下运行：scrapy crawl demo

抓取股吧内容的标题和url连接，以字典形式形式输出{标题名：url链接}

----------------------------------------------------------

006save_in_redis_demo.py

获取“股吧”中帖子内容的url链接，

并将获取的内容以集合形式保存在Redis数据库中，方便日后调用

----------------------------------------------------------
