class Solution:
    def longestCommonPrefix(self, strs):
        # THIS SOLUTION HAS INDEX OUT OF RANGE ERRORS
        prefix = strs[0]
        have_similar_prefix = None
        if len(strs) > 1:
            have_similar_prefix = prefix[0] == strs[1][0]
        else:
            have_similar_prefix = False
            
        for str in strs:
            if len(str) > 0 and len(prefix) > 0:
                i = 0
                cur_chars_equal = str[i] is prefix[i]
                shorter = (str if len(str) < len(prefix) else prefix)
                
                while cur_chars_equal is True and i < len(shorter) - 1:
                    i += 1
                    if str[i] is not prefix[i]:
                        cur_chars_equal = False
                        prefix = shorter[:i]
                    
                if cur_chars_equal:
                    prefix = shorter

        if have_similar_prefix:
            return prefix
        else:
            return ""
            

class TestCase:
    def test(self, solution, strs):
        print(solution.longestCommonPrefix(strs))

SolutionTester = TestCase()
mySolution = Solution()

SolutionTester.test(mySolution, ["flower","flow","flight"])
SolutionTester.test(mySolution, ["dog","racecar","car"])