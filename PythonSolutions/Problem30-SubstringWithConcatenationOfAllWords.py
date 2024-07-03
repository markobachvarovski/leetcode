from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length = len(words[0])
        num_words = len(words)
        total_length = word_length * num_words
        word_count = Counter(words)
        result_indices = []

        # Iterate over each possible starting point within the first word_length characters
        for i in range(word_length):
            left = i
            right = i
            seen_words = {}
            count = 0

            while right + word_length <= len(s):
                word = s[right:right + word_length]
                right += word_length

                if word in word_count:
                    if word not in seen_words:
                        seen_words[word] = 1
                    else:
                        seen_words[word] += 1
                    count += 1

                    while seen_words[word] > word_count[word]:
                        left_word = s[left:left + word_length]
                        seen_words[left_word] -= 1
                        count -= 1
                        left += word_length

                    if count == num_words:
                        result_indices.append(left)
                else:
                    seen_words.clear()
                    count = 0
                    left = right

        return result_indices

        # Alternative solution
        # n = len(words)
        # word_len = len(words[0])
        # ansArray = []
        # dict = {}
        #
        # for word in words:
        #     if word in dict:
        #         dict[word] += 1
        #     else:
        #         dict[word] = 1
        #
        # for l in range(0, len(s)):
        #     success = True
        #     seen = {}
        #     for r in range(l, l + n*word_len, word_len):
        #         word = s[r:r+word_len]
        #         if word in dict:
        #             if word in seen:
        #                 seen[word] += 1
        #             else:
        #                 seen[word] = 1
        #
        #             if seen[word] > dict[word]:
        #                 success = False
        #                 break
        #         else:
        #             success = False
        #             break
        #
        #     if success:
        #         ansArray.append(l)
        #
        # return ansArray

if __name__ == '__main__':
    testStrings = {
        1: ["barfoothefoobarman", ["foo","bar"]],
        2: ["wordgoodgoodgoodbestword", ["word","good","best","word"]],
        3: ["barfoofoobarthefoobarman", ["bar","foo","the"]],
        4: ["wordgoodgoodgoodbestword", ["word","good","best","good"]],
        5: ["lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]]
    }

    for key in testStrings:
        print(f"The possible substrings in {testStrings[key][0]} are: {Solution().findSubstring(testStrings[key][0], testStrings[key][1])}")

