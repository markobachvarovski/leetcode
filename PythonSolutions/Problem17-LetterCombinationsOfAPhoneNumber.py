from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digitsToLetters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        answers = []
        def addLetter(index, currCombination):
            if index == len(digits):
                answers.append(currCombination)
                return

            for letter in digitsToLetters[digits[index]]:
                addLetter(index + 1, currCombination + letter)

        addLetter(0, "")

        return answers

if __name__ == '__main__':
    testCases = {
        1: "23",
        2: "467",
        3: ""
    }

    for key in testCases:
        print(Solution().letterCombinations(testCases[key]))