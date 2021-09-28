# -*-coding:utf-8-*-

import base64
import datetime
import time

import get_kb
import get_week
import in_week
import login


def tras(res_ls, date):  # 将获取的课程信息转换为ics格式输出
    res = ''
    for i in res_ls:
        course_name = i['name']
        course_teacher = i['teacher']
        course_classroom = i['pos']
        year_month_day = (time_now + datetime.timedelta(eval(i['day']) - 1)).strftime('%Y%m%d')
        st = year_month_day + 'T' + i['start_time']
        ft = year_month_day + 'T' + i['end_time']
        res += "BEGIN:VCALENDAR\nPRODID:-//Google Inc//Google Calendar 70.9054//EN\nVERSION:2.0\nCALSCALE:GREGORIAN\nMETHOD:PUBLISH\nX-WR-CALNAME:课程表\nX-WR-TIMEZONE:America/New_York\nBEGIN:VEVENT\n"
        res += "DTSTART:" + st + '\n'
        res += "DTEND:" + ft + '\n'
        res += "DTSTAMP:" + st + '\n'
        res += "UID:课程表\n"
        res += "CREATED:" + st + '\n'
        res += "DESCRIPTION:" + course_teacher + '\n'
        res += "LAST-MODIFIED:" + st + '\n'
        res += "LOCATION:" + course_classroom + '\n'
        res += "SEQUENCE:0" + '\n'
        res += "STATUS:CONFIRMED" + '\n'
        res += "SUMMARY:" + course_name + '\n'
        res += "TRANSP:OPAQUE\nEND:VEVENT\nEND:VCALENDAR\n"
    return res


jie_to_time = {
    '01': '080000',
    '02': '094000',
    '03': '100000',
    '04': '114000',
    '05': '140000',
    '06': '154000',
    '07': '160000',
    '08': '174000',
    '09': '190000',
    '10': '204000'
}

if __name__ == '__main__':
    username_tmp = '19405620001'
    passwd_tmp = 'lkjh4010027'
    encode_username = base64.b64encode(username_tmp.encode("utf-8")).decode('utf-8')
    encode_passwd = base64.b64encode(passwd_tmp.encode("utf-8")).decode('utf-8')
    encode = encode_username + "%%%" + encode_passwd
    cookies = login.login(encode)
    class_ls_tmp = get_kb.get_kb(cookies)
    now_week = get_week.get_now_week(cookies)
    finnal_week = get_week.get_all_week(cookies)
    res_ls = []
    class_ls = []
    for i in class_ls_tmp:
        dist_tmp = {}
        for j in i:
            if j == 'class':
                st = i['class'][0:2]
                ed = i['class'][3:5]
                dist_tmp['start_time'] = jie_to_time[st]
                dist_tmp['end_time'] = jie_to_time[ed]
                continue
            dist_tmp[j] = i[j]
        class_ls.append(dist_tmp)
    time_now = datetime.date.today()
    if time_now.isoweekday() != 1:
        time_now -= datetime.timedelta(time_now.isoweekday() - 1)

    print(class_ls)
    ans = ""
    for week in range(eval(now_week), eval(finnal_week) + 1):
        for item in class_ls:
            if in_week.in_week(str(week), item['weeks']):
                if item['week_flag'] == '单周' and int(week) % 2 == 1:
                    res_ls.append(item)
                elif item['week_flag'] == '双周' and int(week) % 2 == 0:
                    res_ls.append(item)
                elif item['week_flag'] == '每周':
                    res_ls.append(item)
        ans += tras(res_ls, time_now)
        res_ls=[]
        time_now += datetime.timedelta(7)
    f = open("your_calendar.ics", mode='w', encoding="utf-8")
    f.write(ans)
    f.close()
