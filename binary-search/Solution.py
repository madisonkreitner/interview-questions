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

        # sorted in ascending order, so we can use a binary search
        # first we need a pointer
        left = 0
        right = len(nums) - 1
        pivot = len(nums) // 2
        while left <= right:
            pivot = left + (right - left) // 2
            if target == nums[pivot]:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1

class TestCase:
    def test(self, solution, nums, target):
        print(solution.binarySearch(nums, target))

SolutionTester = TestCase()
mySolution = Solution()

SolutionTester.test(mySolution, [2,7,11,15,17,20,21], 18) #not in list
SolutionTester.test(mySolution, [2,7,11,15,17,20,21], 20)
SolutionTester.test(mySolution, [2,3,4,6,7], 6)
SolutionTester.test(mySolution, [3,4,5,6,7,8,9,10,11,12,13,14], 6)