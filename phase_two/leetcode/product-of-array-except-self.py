class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        index = 1
        last_index = 1
        pre =[]
        sef = []
        answer = []
        for i in range(len(nums)):
            index=index*nums[i]
            last_index = last_index * nums[-1-i]
            pre.append(index)
            sef.append(last_index)
        sef = sef[::-1]
        for i in range(len(nums)):
            
            if i == 0:
                answer.append(sef[i+1])
            elif i == len(nums)-1:
                answer.append(pre[i-1])
            else:
                answer.append(sef[i+1]*pre[i-1])

        return answer
        