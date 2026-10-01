from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ord = sorted(nums)
        seen = {}
        for i, num in enumerate(ord):
            if num not in seen:
                seen[num] = i
        
        res = []

        for num in nums:
            res.append(seen[num])
        return res