import operator
class Solution(object):
    def evalRPN(self, tokens):
        operators = {'+': operator.add, '-': operator.sub, 
                '*': operator.mul, '/':operator.truediv }
        stack = []
        for j in tokens:
            if j not in operators:
                stack.append(int(j))
            else:
                right,left = stack.pop(),stack.pop()
                stack.append(int(operators[j](left,right)))
        return stack.pop()
