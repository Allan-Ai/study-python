#sameple2
# -*- coding: UTF-8 -*-
'''
实例2
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
'''

question = "实例2\
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20\万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元\的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数"
print question

def bonus(rev):
    print "revenue is {}".format(rev)
    if (rev <= 10):
        return (rev*0.1)
    elif (rev <= 20):
        return (bonus(10) + (rev - 10)*0.075)
    elif (rev <= 40):
        return (bonus(20) + (rev - 20)*0.05)
    elif (rev <= 60):
        return (bonus(40) + (rev - 40)*0.03)
    elif (rev <= 100):
        return (bonus(60) + (rev - 60)*0.015)
    else:
        return (bonus(100) + (rev - 100)*0.01)

revenue = input("Plase input the rev:")
print "Bonus is {}".format(bonus(revenue))

i = int(raw_input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        print r
        r = r + (i-arr[idx])*rat[idx]
        print (i-arr[idx])*rat[idx]
        i=arr[idx]
print r
