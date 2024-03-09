class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters)-1
        res = letters[0]
        while l<=r:
            mid = l+(r-l)//2
            if letters[mid]>target:
                if letters[mid]!=target:
                    res = letters[mid]
                r = mid -1
            else:
                l = mid +1
        return res
        