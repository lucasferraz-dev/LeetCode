class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seenS = {}
        seenT = {}

        for i in s:
            if i not in seenS:
                seenS[i] = 1
            else:
                seenS[i] += 1
        
        for j in t:
            if j not in seenT:
                seenT[j] = 1
            else:
                seenT[j] += 1
        
        return(seenS == seenT)

