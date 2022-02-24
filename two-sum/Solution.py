class Solution:
    def twoSum(self, nums, target):
        indeces = [0,0]

        for i in range(len(nums)):
            slice = nums[i+1:]
            for j in range(len(slice)):
                if nums[i] + slice[j] == target:
                    indeces = [i,j+1]
                    values = [nums[i], slice[j]]
                    print(indeces, values, target)
                    return
        

class TestCase:
    def test(self, solution, nums, target):
        solution.twoSum(nums, target)

SolutionTester = TestCase()
mySolution = Solution()

SolutionTester.test(mySolution, [2,7,11,15], 9)
SolutionTester.test(mySolution, [3,2,4], 6)
SolutionTester.test(mySolution, [3,3], 6)