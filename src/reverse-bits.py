# url https://leetcode.com/problems/reverse-bits/
# writtenby:anhty9le


def binary(n):
    arr = []

    while n != 0:
        arr.append(n % 2)
        n = n // 2
    while len(arr) < 32:
        arr.append(0)

    return arr


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        arr = (binary(n))
        n = len(arr)
        sum = 0

        for i in range(n):
            sum += arr[i] * 2**(n - i - 1)

        return sum
