class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_exponent = False
        seen_decimal = False
        seen_digit_after_e = False

        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
                if seen_exponent:
                    seen_digit_after_e = True
            elif char in ['+', '-']:
                if i != 0 and s[i - 1] not in ['e', 'E']:
                    return False
            elif char == '.':
                if seen_exponent or seen_decimal:
                    return False
                seen_decimal = True
            elif char in ['e', 'E']:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
            else:
                return False

        return seen_digit and (not seen_exponent or seen_digit_after_e)

if __name__ == '__main__':
    testCases = {
        1: "0",
        2: "e",
        3: ".",
        4: "2",
        5: "0089",
        6: "-0.1",
        7: "+3.14",
        8: "4.",
        9: "-.9",
        10: "2e10",
        11: "-90E3",
        12: "3e+7",
        13: "+6e-1",
        14: "53.5e93",
        15: "-123.456e789",
        16: "abc",
        17: "1a",
        18: "1e",
        19: "e3",
        20: "99e2.5",
        21: "--6",
        22: "-+3",
        23: "95a54e53"
    }

    for key in testCases:
        print(Solution().isNumber(testCases[key]))
