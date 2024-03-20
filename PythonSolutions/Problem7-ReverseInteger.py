class Solution:
    def reverse(self, x: int) -> int:
        isNegative = x < 0
        arr = [int(digit) for digit in str(abs(x))]

        for i in range(0, len(arr) // 2):
            temp = arr[i]
            arr[i] = arr[-(i+1)]
            arr[-(i+1)] = temp

        if isNegative:
            sol = -1 * int(''.join(map(str, arr)))
            if sol > (-2)**31:
                return sol
        else:
            sol = int(''.join(map(str, arr)))
            if sol < 2**31 - 1:
                return sol

        return 0



if __name__ == '__main__':
    testInts = {
        1: 123,
        2: -123,
        3: 1534236469
    }

    for key in testInts:
        print(f"The reverse digit conversion of {testInts[key]} is: {Solution().reverse(testInts[key])}")
