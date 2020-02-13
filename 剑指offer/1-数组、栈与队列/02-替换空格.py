'''
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        result = ''
        for i in s:
            if i == ' ':
                result = result + '%20'
            else:
                result = result + i
        return result
                
a = Solution()
print(a.replaceSpace('hello world'))

'''
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        strLen = len(s)
        # 定义空字符串准备接收
        rep_str = ''
        # 遍历，检测到空格就加上"%20"
        for i in range(strLen):
            if s[i].isspace():
                rep_str += '%'
                rep_str += '2'
                rep_str += '0'
            else:
                rep_str += s[i]
        # 返回辅助字符串
        return rep_str
'''