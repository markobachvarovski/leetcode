from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        ans = [0] * n
        stack = []

        for log in logs:
            function, state, time = log.split(":")
            function, time = int(function), int(time)

            if state == 'start':
                if stack:
                    prev_id, prev_start = stack[-1]
                    ans[prev_id] += time - prev_start
                stack.append([function, time])
            else:
                prev_function, prev_time = stack.pop()
                ans[prev_function] += time - prev_time + 1

                if stack:
                    stack[-1][1] = time + 1

        return ans



if __name__ == '__main__':
    testCases = {
        1: [3, ["0:start:0", "2:start:4", "2:end:5", "1:start:7", "1:end:10", "0:end:11"]],
        2: [1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]],
        3: [2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]]
    }

    for key in testCases:
        print(Solution().exclusiveTime(testCases[key][0], testCases[key][1]))
