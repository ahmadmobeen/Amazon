#https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for i in range(len(s)):
            
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif s[i] == ')':
                ch = stack.pop()
                if ch != '(':
                    return False
            elif s[i] == ']':
                ch = stack.pop()
                if ch != '[':
                    return False
            elif s[i] == '}':
                ch = stack.pop()
                if ch != '{':
                    return False
        return not len(stack)
