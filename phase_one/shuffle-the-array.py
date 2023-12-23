class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first = nums[:n]
        last = nums[n:]
        ptr = 0
        ptr1=0
        while ptr1!=n:
            first.insert(ptr+1,last[ptr1])
            ptr+=2
            ptr1+=1

        return first
        