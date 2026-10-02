class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        res = []
        maj = max(candies)
        for i in candies:
            res.append(i + extraCandies >= maj)
        return res