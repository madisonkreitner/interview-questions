from email.utils import decode_params


class Solution:
    def addBinary(self, a, b):
        # convert each string to binary
        a_in_dec = 0
        for index, char in enumerate(reversed(a)):
            if char == "1":
                a_in_dec += 2 ** index

        b_in_dec = 0
        for index, char in enumerate(reversed(b)):
            if char == "1":
                b_in_dec += 2 ** index

        # add numbers
        mysum = a_in_dec + b_in_dec

        # convert back to binary string
        output = bin(mysum)[2:]

        return output


class SolutionTester:
    def test(self, solution, a, b):
        print(solution.addBinary(a, b))


tester = SolutionTester()
mySolution = Solution()

tester.test(mySolution, "1010", "1011")  # "1"
tester.test(mySolution, "11", "1")  # "100"
