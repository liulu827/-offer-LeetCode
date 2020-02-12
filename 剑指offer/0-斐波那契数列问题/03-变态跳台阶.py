'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
# 从第n阶往前跳：f(n) = f(n-1)+f(n-2)+f(n-3)+...+f(1)
# 第n-1阶往前跳：f(n-1) = f(n-2)+f(n-3)+...+f(1)
# f(n) = 2f(n-1)
class Solution:
    def jumpFloorII(self, number):
        # write code here
        # 考虑边界条件：n=1 ==> 1;n=2 ==> 2
        if number > 0:
            a = 1
            b = 2
            for _ in range(number-1):
                a, b = b, 2*b
            return a
        return None

result = Solution()
for number in range(30):
    print(result.jumpFloorII(number))
