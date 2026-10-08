class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen = {}

        for i in magazine:
            seen[i] = seen.get(i,0) + 1

        for i in ransomNote:
            if i in seen and seen[i] > 0:
                seen[i] -= 1
            else:
                return False
        return True
