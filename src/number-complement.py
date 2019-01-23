# url https://leetcode.com/problems/number-complement/
# writtenby:anhty9le


def binary(num):
    arr = []

    while num != 0:
        arr.append(num % 2)
        num = num // 2

    return arr


def prime(num):
    if num < 2:
        return False

    result = True
    i = 2
    n = int(math.sqrt(num))

    while i < n or result is False:
        if n % i != 0:
            result = False
        i += 1

    return result


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        arr = binary(num)
        n = len(arr)

        for i in range(n):
            if arr[i] == 0:
                arr[i] = 1
            else:
                arr[i] = 0

        sum = 0

        for i in range(n):
            sum += arr[i] * math.pow(2, i)
            print(i)

        return int(sum)
