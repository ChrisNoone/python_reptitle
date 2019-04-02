# coding: utf-8

from urllib import request, parse
from http import cookiejar

# 创建cookiejar的实例
cookie = cookiejar.CookieJar()
# 生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor()
# 创建http请求管理器
http_handler = request.HTTPHandler()
# 创建https请求管理器
https_handler = request.HTTPSHandler()
# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)


def login():
    """
    负责初次登录
    需要输入用户名密码，用来获取登录cookie凭证
    """
    url = 'https://login.taobao.com/member/login'
    data = {
        'TPL_username_1': '981400112@qq.com',
        'TPL_password_1': 'Lv8023_Alibaba'
    }
    data = parse.urlencode(data)
    seq = request.Request(url, data=data.encode())
    opener.open(seq)


def main_page():
    url = 'https://shoucang.taobao.com/item_collect.htm?spm=a2e15.8261149.1997525053.2.474429b4O529UJ'

    rsp = opener.open(url)
    html = rsp.read().decode()

    with open('rsp.html', 'w') as f:
        f.write(html)
    f.close()


login()
main_page()
