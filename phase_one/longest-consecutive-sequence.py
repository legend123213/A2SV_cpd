class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # ma = 0
        # counter = 0
        # sett = set(nums)
        # nums = list(sett)
        # num = sorted(nums)
        # print(num)
        # for i in range(len(num)-1):
        #     if num[i+1]-num[i] == 1:
        #         counter = counter + 1
        #         if i == len(num)-2:
        #             ma = counter
        #             counter = 0 
           
        #     else:
        #         if ma <= counter:
        #             ma = counter
        #             counter = 0 
        #     print(f"{counter} and {ma}")
        # print(ma)     
        # return ma+1 if len(num)!=0 else ma
        i =0 
        j = 1
        counter = 0
        ma = 0
        nums= list(set(nums))
        nums.sort()
        print(nums)
        if len(nums)==0:
            return 0
        while j<len(nums):
            if nums[j]- nums[i] == j-i:
                j+=1
                counter +=1
            else:
                ma = max(ma,counter)
                counter = 0
                i=j
                j+=1
            ma= max(ma,counter)
        return ma+1
            

            

        