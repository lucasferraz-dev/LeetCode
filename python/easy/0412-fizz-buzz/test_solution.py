from solution import Solution


solution = Solution()

tests = [
    (
        3,
        ["1", "2", "Fizz"]
    ),
    (
        5,
        ["1", "2", "Fizz", "4", "Buzz"]
    ),
    (
        15,
        [
            "1", "2", "Fizz", "4", "Buzz",
            "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz"
        ]
    ),
]


for n, expected in tests:
    result = solution.fizzBuzz(n)

    if result == expected:
        print(f"✅ Passed: n = {n}")
    else:
        print(f"❌ Failed: n = {n}")
        print(f"   Expected: {expected}")
        print(f"   Got:      {result}")