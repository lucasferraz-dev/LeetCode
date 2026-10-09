class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        cont = 0
        best = 0
        for i in nums:
            if i == 1:
                cont += 1
                best = max(best, cont)
            else:
                cont = 0
        return best