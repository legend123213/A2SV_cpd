class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        st = list(palindrome)
        for i in range(len(palindrome)):
            if i!= len(palindrome)//2 and st[i]!="a":
                st[i]="a"
                break
        else:
            st[-1] = "b"
        return "".join(st)
        