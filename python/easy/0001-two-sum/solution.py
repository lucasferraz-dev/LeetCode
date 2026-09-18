class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for itens in range(len(nums)):
            if target - nums[itens] in seen:
                return [seen[target - nums[itens]], itens]
            seen[nums[itens]] = itens
        return []
