class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        even = 0
        for num in nums:
            cont = 0
            while num > 0:
                cont += 1
                num //= 10
            if cont % 2 == 0:
                even += 1
        return even