class Solution:
    def isHappy(self, n: int) -> bool:
        se = set()
        nu = 0
        k = str(n)
        while True:
            counter = 0
            print(se)
            for i in k:
                counter+=int(i)**2
            if nu>len(se):
                if counter == 1:
                    return True
                else:
                    return False
            se.add(counter)
            k=str(counter)
            nu+=1
            counter=0
        
