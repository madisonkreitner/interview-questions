class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return (i, j)
        

class TestCase:
    def test(self, solution, nums, target):
        print(solution.twoSum(nums, target))

SolutionTester = TestCase()
mySolution = Solution()

SolutionTester.test(mySolution, [2,7,11,15], 9)
SolutionTester.test(mySolution, [3,2,4], 6)
SolutionTester.test(mySolution, [3,3], 6)