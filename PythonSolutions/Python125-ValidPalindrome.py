class Solution:
    def isPalindrome(self, s: str) -> bool:

        frontPointer = 0
        backPointer = len(s) - 1

        while frontPointer < backPointer:
            if not s[frontPointer].isalnum():
                frontPointer += 1
                continue

            if not s[backPointer].isalnum():
                backPointer -= 1
                continue

            if s[frontPointer].lower() != s[backPointer].lower():
                return False

            frontPointer += 1
            backPointer -= 1

        return True

if __name__ == '__main__':
    testStrings = {
        1: "race a car",
        2: "A man, a plan, a canal: Panama"
    }

    for key in testStrings:
        if Solution().isPalindrome(testStrings[key]):
            print(f"{testStrings[key]} is a palindrome")
        else:
            print(f"{testStrings[key]} is not a palindrome")
