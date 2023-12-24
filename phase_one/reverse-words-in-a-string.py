class Solution:
    def reverseWords(self, s: str) -> str:
        k = s.split()
        i = ' '.join(k[::-1])
        return i