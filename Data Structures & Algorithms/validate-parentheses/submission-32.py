class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else:
                if not stack:
                    return False
                elif char == ")":
                    if stack[-1] != "(":
                        return False
                    else:
                        stack.pop()
                elif char == "]":
                    if stack[-1] != "[":
                        return False
                    else:
                        stack.pop()
                else:
                    if stack[-1] != "{":
                        return False
                    else:
                        stack.pop()
        if not stack:
            return True
        else:
            return False