# coding: utf-8

from urllib import request, error

if __name__ == '__main__':
    url = 'https://www.google.com/123'

    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        data = rsp.read().decode()
        print(data)

    except error.HTTPError as e:
        print('HTTPError: {0}'.format(e.reason))

    except error.URLError as e:
        print('URLError: {0}'.format(e.reason))

    except Exception as e:
        print(e)
