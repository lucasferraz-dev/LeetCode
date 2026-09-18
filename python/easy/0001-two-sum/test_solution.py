from solution import Solution

solution = Solution()

tests = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
]

for nums, target, expected in tests:
    result = solution.twoSum(nums, target)

    if result == expected:
        print(f"✅ Passed: {nums}, target={target}")
    else:
        print(f"❌ Failed: {nums}, target={target}")
        print(f"   Expected: {expected}")
        print(f"   Got:      {result}")