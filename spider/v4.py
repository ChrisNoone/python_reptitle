# coding: utf-8

from urllib import request, error

if __name__ == '__main__':
    url = 'http://www.baidu.com'

    # 设置代理地址
    proxy = {'http': '221.223.42.227:8060'}
    # 创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 创建Opener
    opener = request.build_opener(proxy_handler)
    # 安装Opener
    request.install_opener(opener)

    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
