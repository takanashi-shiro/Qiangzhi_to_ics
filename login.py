import bs4
import requests
import base64


def login(encode):
    # encode_username = base64.b64encode(username.encode("utf-8")).decode('utf-8')
    # encode_passwd = base64.b64encode(passwd.encode("utf-8")).decode('utf-8')
    # encode = username + "%%%" + passwd
    url = "http://218.75.197.123:83/jsxsd/xk/LoginToXk"
    headers = {
        'Host': '218.75.197.123:83',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'http://218.75.197.123:83',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://218.75.197.123:83/jsxsd/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '91',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    params = {
        'userAccount': "",
        'userPassword': "",
        'encoded': encode
    }
    # response = requests.request(method='POST',url=url, headers=headers,data=params)
    session = requests.session()
    session.post(url=url, headers=headers, data=params)
    return session


# if __name__ == "__main__":
#     print(login('MTk0MDU2MjAwMDE=%%%bGtqaDQwMTAwMjc='))
