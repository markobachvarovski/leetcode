from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        currentDirectionIndex = 0

        visited = set()
        i, j = 0, 0
        answer = []

        while len(visited) < rows * cols:
            if 0 <= i < rows and 0 <= j < cols and (i, j) not in visited:
                visited.add((i, j))
                answer.append(matrix[i][j])
            else:
                # Backtrack and change direction
                i -= directions[currentDirectionIndex][0]
                j -= directions[currentDirectionIndex][1]

                currentDirectionIndex = (currentDirectionIndex + 1) % 4

            i += directions[currentDirectionIndex][0]
            j += directions[currentDirectionIndex][1]

        return answer


if __name__ == '__main__':
    testCases = {
        1: [[1,2,3],[4,5,6],[7,8,9]],
        2: [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    }

    for key in testCases:
        print(f"{Solution().spiralOrder(testCases[key])}")
