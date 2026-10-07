class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        seen = {}
        cont = 0
        for i in nums:
            if i in seen:
                cont += seen[i]
                seen[i] += 1
            else:
                seen[i] = 1
        return cont