import base64
import functools
import requests
import bs4

import login


def mycmp(a, b):
    if eval(a['day']) < eval(b['day']):
        return -1
    elif eval(a['day']) > eval(b['day']):
        return 1
    else:
        return 0


def get_kb(session):
    url = "http://218.75.197.123:83/jsxsd/xskb/xskb_list.do"
    headers = {
        'Host': '218.75.197.123:83',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://218.75.197.123:83/jsxsd/framework/xsMain.jsp',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive'
    }
    response = session.get(url=url, headers=headers)
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    # print(soup)

    ls = soup.find_all('div', class_="kbcontent")
    class_list = []
    tmp_dicts_ls = ['name', 'teacher', 'weeks', 'week_flag', 'day', 'class', 'pos']
    for i in ls:
        if len(i.text) != 1:
            tt = 0
            tmp_dicts = {}
            for j in i:
                if len(j.text) != 0:
                    if j.text == '&nbspP' or j.text =='&nbspO':
                        continue
                    if tt == 2:
                        weeks = j.text[0:j.text.find('(')]
                        week_flag = j.text[j.text.find('(') + 1:j.text.find(')')]
                        if week_flag == '周':
                            week_flag = "每周"
                        day = str(i['id'])[-3:-2:]
                        classtime = j.text[j.text.find('[') + 1:j.text.find(']')]
                        tmp_dicts['weeks'] = weeks
                        tmp_dicts['week_flag'] = week_flag
                        tmp_dicts['day'] = day
                        tmp_dicts['class'] = classtime
                        tt += 4
                    else:
                        if j.text[0] == '-' and j.text[1] == '-':
                            tt = 0
                            continue
                        tmp_dicts[tmp_dicts_ls[tt]] = j.text
                        tt += 1
                        if tt >= 7:
                            # print(tmp_dicts)
                            class_list.append(tmp_dicts)
                            tmp_dicts={}
    res = sorted(class_list, key=functools.cmp_to_key(mycmp))
    return res


# if __name__ == "__main__":
#     username_tmp = '19405620013'
#     passwd_tmp = 'wyj2001205'
#     encode_username = base64.b64encode(username_tmp.encode("utf-8")).decode('utf-8')
#     encode_passwd = base64.b64encode(passwd_tmp.encode("utf-8")).decode('utf-8')
#     encode = encode_username + "%%%" + encode_passwd
#     cookies = login.login(encode)
#     res_ls = get_kb(cookies)
    #print(res_ls)
#     class_map = {
#         'name': '课程',
#         'teacher': '教师',
#         'weeks': '上课周次',
#         'week_flag': '上课标记',
#         'day': '星期',
#         'class': '节次',
#         'pos': '上课地点'
#     }
#     res = ""
#     for i in res_ls:
#         for keys in i:
#             res += class_map[keys] + " : " + i[keys] + "\n"
#         res+="========\n"
#     print(res)
#     ls = [1]
#     print(len(ls)==1)
