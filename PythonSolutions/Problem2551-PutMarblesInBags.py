from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1 or k == len(weights):
            return 0

        score_contribution = []
        for i in range(0, len(weights) - 1):
            score_contribution.append(weights[i] + weights[i + 1])

        score_contribution.sort()

        minimal_score = sum(score_contribution[0:k - 1])
        maximal_score = sum(score_contribution[-k + 1:])

        return maximal_score - minimal_score


if __name__ == '__main__':
    testCases = {
        1: [[1,3,5,1], 2],
        2: [[1, 3], 2]
    }

    for key in testCases:
        print(Solution().putMarbles(testCases[key][0], testCases[key][1]))