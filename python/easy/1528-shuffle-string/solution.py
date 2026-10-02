class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        res = [""] * len(s)
        for i in range(len(s)):
            res[indices[i]] = s[i]
        res = "".join(res)
        return res