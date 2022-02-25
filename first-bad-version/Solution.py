class Solution:
    def firstBadVersion(self, n, bad):
        left = 1
        right = n
        current = (right - left) // 2 if (right - left) // 2 > 0 else 1


        while True:
            if self.isBadVersion(current, bad) is False:
                left = current
                current = left + (right - left) // 2
            else:
                if self.isBadVersion(current - 1, bad) is False:
                    return current
                right = current
                current = left + (right - left) // 2

    def isBadVersion(self, version, bad):
        if version == bad:
            return True
        return False

class TestCase:
    def test(self, solution, n, bad):
        print(solution.firstBadVersion(n, bad))

SolutionTester = TestCase()
mySolution = Solution()

SolutionTester.test(mySolution, 5, 4)
SolutionTester.test(mySolution, 1, 1)