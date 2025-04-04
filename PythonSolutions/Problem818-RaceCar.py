from collections import deque


class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])
        visited = set()
        visited.add((0,1))

        while queue:
            pos, speed, moves = queue.popleft()

            if pos == target:
                return moves

            next_pos, next_speed = pos + speed, speed * 2
            if (next_pos, next_speed) not in visited:
                visited.add((next_pos, next_speed))
                queue.append((next_pos, next_speed, moves + 1))

            reverse_speed = -1 if speed > 0 else 1
            if (pos, reverse_speed) not in visited:
                visited.add((pos, reverse_speed))
                queue.append((pos, reverse_speed, moves + 1))

        return -1

if __name__ == '__main__':
    testCases = {
        1: 3,
        2: 6
    }

    for key in testCases:
        print(Solution().racecar(testCases[key]))
