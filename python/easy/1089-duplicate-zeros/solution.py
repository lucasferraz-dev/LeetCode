class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        j = len(arr) - 1
        i = 0
        while i < j:
            if arr[i] == 0:
                arr.insert(i, 0)
                i += 2
                arr.pop()
            else:
                i += 1
