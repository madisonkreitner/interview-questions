# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def binarySearch(self, nums, target):
        # O(n) time complexity
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1

        #sorted in ascending order, so we can use a binary search
        #first we need a pointer
        pass
        

class TestCase:
    def test(self, solution, nums, target):
        solution.binarySearch(nums, target)

SolutionTester = TestCase()
mySolution = Solution()

SolutionTester.test(mySolution, [2,7,11,15], 9)
SolutionTester.test(mySolution, [3,2,4], 6)
SolutionTester.test(mySolution, [3,3], 6)