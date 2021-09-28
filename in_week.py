def in_week(now, weeks):
    week_ls = weeks.split(',')
    for i in week_ls:
        if i.find('-') == -1:
            if eval(i) == eval(now):
                return True
        else:
            st = eval(i[0:i.find('-')])
            ed = eval(i[i.find('-') + 1:])
            if ed >= eval(now) >= st:
                return True
    return False

if __name__ == '__main__':
    print(in_week('2','1-7,9-10'))