# url https://leetcode.com/problems/binary-number-with-alternating-bits/
# writtenby:anhty9le


def binary(num):
    arr = []

    while num != 0:
        arr.append(num % 2)
        num = num // 2

    return arr


class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        arr = binary(n)
        k = len(arr)
        Result = True

        for i in range(k - 1):
            if arr[i] == arr[i + 1]:
                Result = False
                break

        return Result
