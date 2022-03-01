class Solution:
    def removeElement(self, nums, val):
        matches = 0
        for i in range(len(nums)):
            while nums[i] is val:
                if nums[i] is val:
                    matches += 1
                # shift the rest to the left, which will remove the matching one
                last_index = len(nums) - matches
                for j in range(i,last_index):
                    nums[j] = nums[j+1]
                    if j is last_index - 1:
                        nums[last_index] = None

                if i is last_index:
                    nums[i] = None

        return len(nums) - matches
class TestCase:
    def test(self, solution, nums, val):
        print(solution.removeElement(nums, val))

SolutionTester = TestCase()
mySolution = Solution()

SolutionTester.test(mySolution, [3,2,2,3], 3)
SolutionTester.test(mySolution, [0,1,2,2,3,0,4,2], 2)