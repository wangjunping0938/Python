# -*- coding: utf-8 -*-

# 分解序列为单独变量
p = (4, 5)
x, y = p
print('x=%s, y=%s' %(x, y))

data = ['ACME', 50, 91.1, (2019, 12, 5)]
name, shares, price, date = data
print('name={}, shares={}, price={}, date={}'.format(name, shares, price, date))
name, shares, price, (year, month, day) = data
print('year={}, month={}, day={}'.format(year, month, day))
_, shares, price, _ = data
print(shares, price)


# 从任意长度的可迭代对象中分解元素
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

record = ('Dave', 'dave@example.com', '888-888-1211', '888-888-1122')
name, email, *phone_numbers = record
print('name=%s, email=%s, phone_numbers=%s' %(name, email, phone_numbers))

*trailing, current = [10, 8, 7, 1, 3, 9, 5, 10, 3]
print(current)

# 迭代一个长度变化的序列
record = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in record:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged Uesr:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print('uname={}, homedir={}, sh={}'.format(uname, homedir, sh))

# 丢弃可迭代对象中的部分变量
record = ('ACME', 20, 123.45, (12, 5, 2019))
name, *_, (*_, year) = record
print(name, year)

# 拆分可迭代对象的头部和尾部
items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print('head=%s, tail=%s' %(head, tail))
