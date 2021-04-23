class Solution:
    # 나의 풀이 (Runtime: 32ms, Memory: 14.2MB)
    def isValid(self, string: str) -> bool:
        stack = []
        
        for char in string:

            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                # ')))'와 같이 stack에 한 번도 push되지 않는 경우에 대한 예외처리
                if not stack:
                    return False
                
                parentheses = stack.pop()
                
                if char == ')' and parentheses != '(':
                    return False
                if char == '}' and parentheses != '{':
                    return False
                if char == ']' and parentheses != '[':
                    return False
        
        # '((('와 같이 한 번도 pop되지 않는 경우에 대한 예외처리
        return True if len(stack) == 0 else False