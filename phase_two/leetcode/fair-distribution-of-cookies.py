class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        min_unfair = float("inf")
        dis = [0]*k
        if len(cookies) == k:
            return max(cookies)
        def backtrack(ind):
            nonlocal min_unfair
            if ind>len(cookies):
                return
            if ind==len(cookies):
                min_unfair = min(min_unfair,max(dis))
                return
            for i in range(k):
                dis[i]+=cookies[ind]
                backtrack(ind+1)
                dis[i]-=cookies[ind]
        backtrack(0)
        return min_unfair
        # dis = []
        # def backtrack(ind,ls):
        #     if ind>=len(cookies):
        #         dis.append(ls)
        #         return
        #     for j in range(k):
        #         ls[j].append(cookies[ind])
        #         backtrack(ind+1,ls)
        #         ls[j].pop()
        # backtrack(0,[[]*k])
        # return dis

        