class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        word = s.split(" ")
        return len(word[-1])