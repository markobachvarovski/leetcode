from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:

        index1 = m - 1
        index2 = n - 1

        for i in range(m+n-1, -1, -1):
            if index2 >= 0:
                if index1 >= 0 and nums1[index1] >= nums2[index2]:
                    nums1[i] = nums1[index1]
                    index1 -= 1
                else:
                    nums1[i] = nums2[index2]
                    index2 -= 1
            else:
                break

        return nums1

if __name__ == '__main__':
    testStrings = {
        1: [[1,2,3,0,0,0], 3, [2,5,6], 3],
        2: [[1], 1, [], 0],
        3: [[0], 0, [1], 1],
        4: [[2,0], 1, [1], 1]
    }

    for key in testStrings:
        print(f"The merged result of {testStrings[key][0]} and {testStrings[key][2]} is: {Solution().merge(testStrings[key][0], testStrings[key][1], testStrings[key][2], testStrings[key][3])}")