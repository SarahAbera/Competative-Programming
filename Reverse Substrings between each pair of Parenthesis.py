class Solution(object):
    def reverseParentheses(self,s):
        stk = []
        reversed = ''
        for char in s :
            if char == '(':
                stk.append(reversed)
                reversed = ''
            elif char == ')':
                reversed = stk.pop() + reversed[::-1]
            else:
                reversed += char
        return reversed
