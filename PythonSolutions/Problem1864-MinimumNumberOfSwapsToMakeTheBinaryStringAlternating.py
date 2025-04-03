from collections import Counter

class Solution:
    def minSwaps(self, s: str) -> int:
        count = Counter(s)

        # 1s and 0s need to differ by at most 1 to be alternating
        if abs(count['1'] - count['0']) > 1:
            return -1

        def generateOptimalSequences(count):

            if count['1'] == count['0']:
                optimalSequence1 = '10' * count['1']
                optimalSequence2 = '01' * count['1']
            elif count['1'] > count['0']:
                optimalSequence1 = '10' * count['0'] + '1'
                optimalSequence2 = optimalSequence1
            else:
                optimalSequence1 = '01' * count['1'] + '0'
                optimalSequence2 = optimalSequence1

            return optimalSequence1, optimalSequence2

        optimalSequence1, optimalSequence2 = generateOptimalSequences(count)

        minSwaps = float('inf')
        mismatches = 0

        for i in range(len(optimalSequence1)):
            if optimalSequence1[i] != s[i]:
                mismatches += 1

        minSwaps = min(minSwaps, mismatches // 2)

        mismatches = 0
        for i in range(len(optimalSequence2)):
            if optimalSequence2[i] != s[i]:
                mismatches += 1

        return min(minSwaps, mismatches // 2)

if __name__ == '__main__':
    testCases = {
        1: "111000", # 1
        2: "010", # 0
        3: "1110", # -1
        4: "01011", # 2
    }

    for key in testCases:
        print(Solution().minSwaps(testCases[key]))
