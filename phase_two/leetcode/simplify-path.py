class Solution:
    def simplifyPath(self, path: str) -> str:
        ls = path.split("/")
        stack = []
        for i in ls:
            if len(stack)!=0 and i == "..":
                stack.pop()
                continue
            if i !="" and i!=".." and i!=".":
                stack.append(i)
        k = "/".join(stack)
        k = "/"+k 
        return k
        