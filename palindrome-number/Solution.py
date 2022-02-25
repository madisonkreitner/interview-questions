class Solution:
    def palindromeNumber(self, x):
        val = str(x)

        if len(val) == 0:
            return False
        elif len(val) == 1:
            return True
        
        left = None
        right = None

        if len(val) % 2 != 0:
            left = len(val) // 2 - 1
            right = len(val) // 2 + 1
        else:
            left = len(val) // 2 - 1
            right = len(val) // 2

        while left >= 0:
            if val[left] != val[right]:
                return False
            left -= 1
            right += 1

        return True
        
        # Also valid is return False if x < 0 else x == int(str(x)[::-1])

class TestCase:
    def test(self, solution, n):
        print(solution.palindromeNumber(n))

SolutionTester = TestCase()
mySolution = Solution()

SolutionTester.test(mySolution, 121)
SolutionTester.test(mySolution, -121)
SolutionTester.test(mySolution, 10)