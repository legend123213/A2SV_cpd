class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            k = s[-i-1]
            s[-i-1]=s[i]
            s[i]=k
        return s
