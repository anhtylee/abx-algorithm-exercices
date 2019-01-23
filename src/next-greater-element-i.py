# url https://leetcode.com/problems/next-greater-element-i/
# writtenby:anhty9le


def position(num, arr):
    k = 0

    for i in range(len(arr)):
        if num == arr[i]:
            k = i
            break

    return k


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        n1 = len(findNums)
        n2 = len(nums)
        Result = []

        for i in range(n1):
            n = position(findNums[i], nums)
            j = n + 1

            while j < n2 and findNums[i] > nums[j]:
                j += 1

            if j >= n2:
                Result.append(-1)
            else:
                Result.append(nums[j])

        return Result
