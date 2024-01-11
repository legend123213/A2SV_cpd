class Solution:
    def sortSentence(self, s: str) -> str:
        k = s.split()
        k.sort(key=lambda x:int(x[-1]))
        k = [k[:len(k)-1] for k in k]
        return ' '.join(k)