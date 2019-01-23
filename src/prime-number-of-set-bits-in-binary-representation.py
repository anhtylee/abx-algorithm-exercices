# url https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
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

    while (i <= n and result == True):
        if num % i == 0:
            result = False
        i += 1

    return result


class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        k = 0
        for num in range(L, R + 1):
            if(prime(sum(binary(num)))):
                k += 1

        return k
