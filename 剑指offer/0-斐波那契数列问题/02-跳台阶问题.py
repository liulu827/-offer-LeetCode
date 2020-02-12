'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''
# n =  1,2,3,4,5,6,7,8
# 跳法 1,2,3,5,
'''
假设青蛙从后面往前方跳，从第n阶跳一次，有两种跳法，跳一级或者跳2级，因此f(n) = f(n-1)+f(n-2)
'''
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # 考虑边界条件
        if number > 0:
            a = 1
            b = 2
            for _ in range(number-1):
                a, b = b, a + b
            return a
        return None

        