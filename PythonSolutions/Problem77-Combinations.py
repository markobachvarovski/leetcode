from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def recursion(l, gen, index, res):
            if len(gen) == k:
                res += [gen[:]]
                return
            for i in range(index, n):
                gen += [l[i]]
                index += 1
                recursion(l, gen, index, res)
                gen.pop()
                index = i + 1

        l = list(range(1, n + 1))
        res = []
        recursion(l, [], 0, res)
        return res

if __name__ == '__main__':
    testCases = {
        1: [4, 2],
    }

    for key in testCases:
        print(f"{Solution().combine(testCases[key][0], testCases[key][1])}")
