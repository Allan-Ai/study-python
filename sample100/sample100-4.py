# sample 4
# -*- coding: UTF-8 -*-
'''
题目：输入某年某月某日，判断这一天是这一年的第几天？

程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
'''
year = int(raw_input('year:\n'))
month = int(raw_input('month:\n'))
day = int(raw_input('day:\n'))

increase = 0
days_in_month = (0, 31, 59, 90, 120, 151, 181, 212, 242, 273, 303, 334)

if (year < 0) or ( month < 1) or (month > 12) or (day < 1) or (day > 31):
    print "input year, month, day are invalid"

if (year % 4 == 0) and (year % 100 != 0) and (year % 400 == 0):
    increase = 1

day_in_month = days_in_month[month-1] + day + increase

print "It is the {}th day.".format(day_in_month)
