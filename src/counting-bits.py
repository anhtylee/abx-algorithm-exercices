# url https://leetcode.com/problems/counting-bits/
# writtenby:anhty9le


def binary(n):
    if n == 0:
        return 0

    arr = []

    while n != 0:
        arr.append(n % 2)
        n = n // 2

    return sum(arr)


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        arr = []

        for i in range(num + 1):
            arr.append(binary(i))

        return arr
