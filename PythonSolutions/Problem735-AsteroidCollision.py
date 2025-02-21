from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            survive = True
            while stack and asteroid < 0 and stack[-1] > 0:
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(asteroid) < stack[-1]:
                    survive = False
                    break
                else:
                    survive = False
                    stack.pop()
                    break
            if survive:
                stack.append(asteroid)
        return stack


if __name__ == '__main__':
    testCases = {
        1: [5,10,-5],
        2: [8, -8],
        3: [10,2,-5],
        4: [-2,-1,1,2]
    }

    for key in testCases:
        print(Solution().asteroidCollision(testCases[key]))
