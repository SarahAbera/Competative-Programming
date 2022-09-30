class Solution(object):
    def isValid(self, s):
        stack = []
        my_par = { ']'  :  '[',
                    '}'  :  '{',
                    ')'  :  '(' }
        for p in s:
            if p in my_par.values():
                stack.append(p)
            elif stack and stack[-1] == my_par[p]:
                stack.pop()
            else :
                return False
        return stack == []
