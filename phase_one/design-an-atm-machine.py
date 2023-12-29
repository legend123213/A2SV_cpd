class ATM:

    def __init__(self):
        self.amountbank = {20: 0, 50: 0, 100: 0, 200: 0, 500: 0}      
    
	
    def deposit(self, banknotesCount: List[int]) -> None:
		   for i ,j in [(0,20),(1,50),(2,100),(3,200),(4,500)]: 
                     self.amountbank[j] += banknotesCount[i]                    


    def withdraw(self, amount: int) -> List[int]:
        ans = [0, 0, 0, 0, 0]

        for i ,j in ((0,500),(1,200),(2,100),(3,50),(4,20)):
                  if amount >= j:    
                        ans[4-i] = min(self.amountbank[j],amount//j)           
                        amount -= ans[4-i] * j

        if amount!=0:
                  return [-1]                                  

        for i,j in [(0,20),(1,50),(2,100),(3,200),(4,500)]:     
                  self.amountbank[j] -= ans[i]                               

        return ans
