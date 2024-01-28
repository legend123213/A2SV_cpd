class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        conn = Counter(blocks[:k])
        count = conn["W"]
        ptr = 0
        ptr_f = k
        while ptr_f < len(blocks):
            if blocks[ptr_f] == "W":
                conn["W"] += 1
            if blocks[ptr] == "W":
                conn["W"] -= 1
            count = min(count, conn["W"])
            ptr += 1
            ptr_f += 1
        return count