from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        if n == 1:
            return ["()"]

        parenthesis = self.generateParenthesis(n - 1)

        for p in parenthesis:
            p_list = list(p)
            p_list.insert(0, ")")
            p_list.insert(0, "(")

            res.append(''.join(p_list))
            last_close_bracket_index = 1
            count = 0

            for i in range(2, len(p_list)):
                if p_list[i] == "(":
                    count += 1
                else:
                    count -= 1

                if count == 0:
                    p_list.insert(i, ")")
                    p_list.pop(last_close_bracket_index)
                    last_close_bracket_index = i
                    res.append(''.join(p_list))

        return res


if __name__ == '__main__':
    testCases = {
        1: [1],
        2: [2],
        3: [3]
    }

    for key in testCases:
        print(f"{Solution().generateParenthesis(testCases[key][0])}")
