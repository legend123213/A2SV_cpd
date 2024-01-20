class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l,r = 0,len(people)-1
        people.sort()
        counter = 0
        while l<=r:
            print(l,r)
            if people[l]+people[r]==limit:
                counter+=1
                l+=1
                r-=1
            elif people[l]+people[r]>limit:
                counter+=1
                r-=1
            else:
                counter+=1
                l+=1
                r-=1

            
        
        return counter 