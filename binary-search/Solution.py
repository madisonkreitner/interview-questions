class Solution:
    def binarySearch(self, nums, target):
        pass

class TestCase:
    def test(self, solution, nums, target):
        solution.binarySearch(nums, target)

SolutionTester = TestCase()
mySolution = Solution()

SolutionTester.test(mySolution, [2,7,11,15], 9)
SolutionTester.test(mySolution, [3,2,4], 6)
SolutionTester.test(mySolution, [3,3], 6)