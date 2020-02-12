'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。 
n<=39 
'''
# -*- coding:utf-8 -*-
# 时间复杂度O(n)，还可以使用递归，时间复杂度太大O(2^n)
class Solution:
    def Fibonacci(self, n):
        # write code here
        # 0,1,1,2,3,5,8 f(n) = f(n-1)+f(n-2)
        if n >= 0:
            a = 0
            b = 1
            for _ in range(n):
                a, b = b, a + b # 把每一步的数据都记录了起来
            return a
        return None

result = Solution()
for n in range(34):
    print(result.Fibonacci(n))
