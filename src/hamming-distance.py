# url https://leetcode.com/problems/hamming-distance/
# writtenby:anhty9le


class Solution(object):
    def binary(self, num):
        s = []
        k = 0

        while (num != 0):
            s.append(num % 2)
            num = num // 2
            k += 1

        return s

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int

        """
        if x > y:
            t = x
            x = y
            y = t

        X = Y = []
        X = self.binary(x)
        Y = self.binary(y)

        n = len(Y)

        for i in range(n - len(X)):
            X.append(0)

        k = 0

        for i in range(len(Y)):
            if X[i] != Y[i]:
                k += 1

        return k
