class Solution(object):
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        operator = '+'

        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char in '+-*/':
                if operator == '+':
                    stack.append(current_number)
                elif operator == '-':
                    stack.append(-current_number)
                elif operator == '*':
                    stack[-1] = stack[-1] * current_number
                elif operator == '/':
                    stack[-1] = int(stack[-1] / current_number)

                operator = char
                current_number = 0

        if operator == '+':
            stack.append(current_number)
        elif operator == '-':
            stack.append(-current_number)
        elif operator == '*':
            stack[-1] = stack[-1] * current_number
        elif operator == '/':
            stack[-1] = int(stack[-1] / current_number)

        return sum(stack)


if __name__ == '__main__':
    testCases = {
        1: "3+2*2",
        2: " 3/2 ",
        3: " 3+5 / 2 "
    }

    for key in testCases:
        print(Solution().calculate(testCases[key]))