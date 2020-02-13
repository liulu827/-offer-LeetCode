'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here

        # 时间复杂度O(n)
        # minNum = 0
        # for i in range(0, len(rotateArray)):
        #     minNum = minNum if minNum  < rotateArray[i] and minNum != 0 else rotateArray[i]
        #
        # return minNum

        # 最小值，一定比前面的要小
        # 二分法查找数据，找左右的方法是：右边的值大于中值，就说明最小值在左边
        # 时间复杂度O(logn)
        # 若数组大小为0
        if not rotateArray:
            # 返回0
            return 0
        # 左侧索引
        left = 0
        # 右侧索引
        right = len(rotateArray) - 1
        # 当左侧索引小于右侧索引时循环
        while left <= right:
            # 中间值为左侧索引和右侧索引求和再除以2，向下取整
            mid = (left + right) >> 1  # (left + right) // 2
            # 若中间索引对应的值小于它左侧的值，即为要取得值
            if rotateArray[mid] < rotateArray[mid - 1]:
                # 返回目标值
                return rotateArray[mid]
            # 若中间索引对应的值小于右侧索引的值，目标值就在左侧
            elif rotateArray[mid] < rotateArray[right]:
                # 将右侧索引置为中间索引-1
                right = mid - 1
            # 反之
            else:
                # 将左侧索引置为中间索引+1
                left = mid + 1

a = Solution()
array = [6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335]
print(len([3,4,5,1,2]))
print(a.minNumberInRotateArray([3,4,5,1,2]))