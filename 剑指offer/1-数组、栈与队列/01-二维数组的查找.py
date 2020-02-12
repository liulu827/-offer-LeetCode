'''
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。
'''
'''
1,2,3
4,5,6
7,8,9
'''
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        i = 0 
        j = len(array[0]) - 1
        while i <= len(array) - 1 and j >= 0:
            if array[i][j] == target:
                return True
            elif array[i][j] > target:
                j -= 1
            else:
                i += 1
        return False


result = Solution()
array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
print(result.Find(5,array))

'''
class Solution:
    # array 二维列表

    # 时间复杂度O(n^2) 291ms ，你没有用到条件递增
    def Find_1(self, target, array):
        # write code here
        for i in range(len(array)):
            for j in range(len(array[i])):
                if target == array[i][j]:
                    return True
        return False

    # 时间复杂度O(n)
    def Find_2(self, target, array):
        # 行数为二维数组的长度
        row_count = len(array)
        i = 0
        # 列数为任意一列的长度
        column_count = len(array[0])
        j = column_count - 1
        # 当i小于行数（即行数,也就是此时的i,取值0--row_count-1）且列数-1大于等于0（即列数，也将就是此时的j,取值0--column_count-1）的时候，循环
        while i < row_count and 0 <= j:
            value = array[i][j]
            if value == target:
                return True
            elif value < target:
                i += 1
            else:
                j -= 1
        return False
'''