class Solution:
    def lengthOfLastWord(self, s: str):
        return len(s.split()[-1].strip())

