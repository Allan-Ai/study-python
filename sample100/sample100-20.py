# -*- coding:UTF-8 -*-
import math

question = "题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？"
print question

n_height = 100*math.pow(0.5,10)
print n_height

def tour(height,n):
    if (n == 1):
        return height
    else:
        return height + tour(height/2,(n -1))

print "The 10th tour is {}".format(tour(100.0,10))
    


