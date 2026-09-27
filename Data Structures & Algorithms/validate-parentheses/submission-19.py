class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for brac in s:
            if brac == "(" or brac == "[" or brac == "{":
                stack.append(brac)
            else:
                if not stack:
                    return False
                elif brac == ")":
                    if stack[-1] != "(":
                        return False
                    else:
                        stack.pop()
                elif brac == "]":
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