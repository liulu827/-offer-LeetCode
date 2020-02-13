'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''
class Solution:
    def __init__(self):
        self.acceptStack = []
        self.outputStack = []
    def push(self, node):
        self.acceptStack.append(node)
    def pop(self):
        if not self.outputStack:
            while self.acceptStack:
                self.outputStack.append(self.acceptStack.pop())
            return self.outputStack.pop()
        else:
            return self.outputStack.pop()

result = Solution()
print(result.push(1),result.push(3),result.pop(),result.push(2),result.pop())