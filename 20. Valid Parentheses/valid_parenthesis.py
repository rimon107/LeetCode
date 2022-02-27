from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        open = ["(", "{", "["]
        close ={
            "(": ")", 
            "{": "}", 
            "[": "]"
            }
        q = deque()

        for parenthesis in s:
            if parenthesis in open:
                q.append(parenthesis)
            else:
                if q:
                    p = q.pop()
                    if parenthesis!=close[p]:
                        return False
                else:
                    return False
        if q:
            return False
        return True
                
