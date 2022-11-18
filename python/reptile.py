# 미래 개체수 예상

cre = {'f':3, 'm':3, 'f_j':6,'m_j':0, 'f_bb':2, 'm_bb':3, 'b':10, 'time':21.5}

def year(f, m):
    if m*3 <= f:
        return m*3 * 6
    else:
        return f * 6
    
# 6개월 후
def future(time):
    for i in range(time):
        new = year(cre['f'], cre['m'])
        cre['f'] += cre['f_j']
        cre['m'] += cre['m_j']
        cre['f_j'] = cre['f_bb']
        cre['m_j'] = cre['m_bb']
        cre['f_bb'] = cre['b']//2
        cre['m_bb'] = cre['b']//2
        cre['b'] = new
        cre['time'] += 0.5

future(1)

# 해칭일 계산

import datetime

def time(x):
    return int(60+(25-x)*10)

def hatching(x, y, m, d):
    day = datetime.datetime(y, m, d)
    a = datetime.timedelta(days = time(x))
    a_p = datetime.timedelta(days = int(time(x) * 0.1))
    m = day + a
    return [m - a_p ,m, m + a_p]

s= hatching(22.5, 2021, 10, 5)

print(s[0].year, '년',
      s[0].month, '월', 
      s[0].day, '일')

print('~')

print(s[1].year, '년',
      s[1].month, '월', 
      s[1].day, '일')

print('~')

print(s[2].year, '년',
      s[2].month, '월', 
      s[2].day, '일')
