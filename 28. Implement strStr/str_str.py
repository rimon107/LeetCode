class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            i = haystack.index(needle)
        except:
            return -1
        return i