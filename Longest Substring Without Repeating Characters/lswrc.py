from collections import deque


class Solution:
    def my_lengthOfLongestSubstring(self, s: str) -> int:
        sub_str = ""
        count = 0
        i = 0
        for char in s:
            if char not in sub_str:
                sub_str += char
                i += 1
            else:
                count = max(count, i)
                a = [pos for pos, ch in enumerate(sub_str) if ch == char]
                sub = sub_str[a[0]+1:]
                sub_str =  sub + char
                i = len(sub_str)
        count = max(count, i)
        return count
    
    def lengthOfLongestSubstringQueue(self, s: str) -> int:
        count = 0
        item = deque()
        for char in s:
            if char not in item:
                item.append(char)
            else:
                count = max(len(item), count)
                while char in item:
                    item.popleft()
                item.append(char)
        count = max(len(item), count)
        return count

    def lengthOfLongestSubstring(self, s: str) -> int:
        # c = self.my_lengthOfLongestSubstring(s)
        c = self.lengthOfLongestSubstringQueue(s)

        return c
