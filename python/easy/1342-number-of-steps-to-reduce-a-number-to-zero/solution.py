class Solution:
    def numberOfSteps(self, num: int) -> int:
        cont = 0
        
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            cont += 1
        return cont