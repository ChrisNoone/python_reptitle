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

- UserAgent
    - 用户代理，简称UA，属于headers的一部分，服务器通过UA判断访问者身份
    - 添加方式有两种：headers 或 add_header()方法
    
- ProxyHander处理（代理服务器）
    - 使用代理ip，是爬虫的重要手段
    - 获取代理服务器的地址：
        - www.xicidaili.com
        - www.goubanjia.com
    - 代理用来隐藏真是访问，代理也不允许频繁访问某一个固定网站，所以代理一定要很多很多
    - 基本使用步骤：
        - 1.设置代理地址
        - 2.创建ProxyHandler
        - 3.创建Opener
        - 4.安装Opener
 
 - cookie & session
    - 由于http协议的无记忆性，人们为了弥补这个缺憾，所采用的一个补充协议
    - cookie是发放给用户的一段信息，session是保存在服务器上的对应的另一半信息，用来记录用户信息
    - cookie和session的区别
        - 存放位置不同
        - cookie不安全
        - session会保存在服务器上，一定时间会过期
        - 单个cookie保存数据不超过4k，很多浏览器限制一个站点最多保存20个
    - session的存放位置
        - 存放在服务器
        - 一般情况下，session是放在内存中或者数据库中
        - 很多情况下不需要人为处理，框架负责处理
        
- SSL
    - SSL证书就是指遵守SSL安全套阶层协议的服务器数字证书（SercureSocketLayer）
    - 由美国网景公司开发
    - CA（CertificateAuthority）是数字证书认证中心，是发放、管理、废除数字证书的收信人的第三方机构

## 4.其它
- ./beautifulsoup/chouti.py 编写笔记
    - beautifulsoup对象的find()和find_all()方法使用
    - find()和find_all()还可以嵌套使用
    - string对象的replace()方法，替换字符
    - python3.x 使用pymysql模块连接mysql数据库
    - execute(sql)方法一次只能接收一条语句并执行，executemany(templet, args)方法可同时接收多条语句并执行，args接收一个元祖列表
    - 字典转元祖，tuple(dict.values())是将字典的values放到一个元祖中
- ./beautifulsoup/github.py 编写笔记
    - cookies = rsp.cookies.get_dict() 提取返回结果中的cookies
    - 使用BeautifulSoup处理的，是返回的Response对象的.text
        - html = BeautifulSoup(rsp.text, 'lxml')
    - requests的get()方法或者post()方法，请求参数中加url、params、headers、cookies等参数
- 字符编码
    - https://juejin.im/post/5ca57998f265da308d50c61a?utm_source=tuicool&utm_medium=referral
    - Python3解释器默认使用UTF-8编码来读 Python2解释器默认使用ASCII来读
    - 在Python3中所有的字符串都是用unicode编码来保存（不需要前面加“u”），字符串的数据类型也只有一个，就是str，只要是用unicode来保存的，那么所有的字符串在任何情况下都不会出现乱码
