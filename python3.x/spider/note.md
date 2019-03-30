## 1. 爬虫准备工作：
- 参考资料：
    - python网络数据采集，图灵工业出版
    - 精通Python爬虫框架Scrapy，人民邮电出版社
    - [python3网络爬虫](http://blog.csdn.net/c406495762/article/details/72858983)
    - [scray官方教程](http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html)

- 前提知识
    - url
    - http协议
    - web前端、html、css、js
    - ajax
    - re、xpath
    - xml
    
## 2. 爬虫简介：
- 爬虫定义：见百度
    - 两大特征：
        - 1.能按照作者的要求下载数据或者内容
        - 2.能自动在网络上流窜
    - 三大步骤：
        - 下载网页
        - 提取正确的信息
        - 根据一定规则自动跳到另外一个网页上执行上两步内容

- 爬虫分类：
    - 通用爬虫
    - 专用爬虫（聚焦爬虫）

- python网络包简介
    - python2.X：urllib，urllib2，urllib3，httplib，httplib2，requests
    - python3.X: urllib，urllib3，httplib2，requests
    
## 3. urllib
- 包含模块
    - urllib.request：打开和读取urls
    - urllib.error：包含urllib.request产生的常见的错误，使用try捕捉
    - urllib.parse：包含解析url的方法
    - urllib.robotparse：解析robots.txt文件

- 网页编码问题解决
    - chardet 可以自动检测页面文件的编码格式，但是可能有有误
    - 需要安装，conda install chardet
    
- urlopen的返回对象
    - geturl：返回请求对象的url
    - info：返回请求对象的meta信息
    - getcode：返回响应的http code
    
- request.data的使用
    - 访问网络的两种方法
        - get：
            - 利用参数给服务器传递信息
            - 参数为dict，然后用parse编码
        - post：
            - 一般向服务器传递参数使用
            - post是把信息自动加密处理
            - 我们如果想使用post信息，需要用到data参数
            - 使用post，意味着http的请求头可能需要更改：
                - Content-Type: application/x-www.form-urlencode
                - Content-Length: 数据长度
                - 简而言之，一旦更改请求方法，请注意其它请求头部信息相适应
            - urllib.parse.urlencode可以将字符串自动转换成上面的
    - request.urlopen()
        - 可以传入url和data
        - 也可以传入一个Request类实例，构造类实例则可以传入url、data、headers等
        
- urllib.error
    - URLError产生的原因：
        - 没网
        - 服务器连接失败
        - 找不到指定服务器
        - 是OSError的子类
    - HTTPError，是URLError的一个子类
    - 两者区别：
         - HTTPError是对应的HTTP请求的返回码错误，如果返回错误码是400以上的，则会引发HTTPError
         - URLError对应的一般是网络出现问题，包括url问题
         - 关系区别：OSError - URLError - HTTPError
         