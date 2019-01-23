# url https://leetcode.com/problems/product-of-array-except-self/
# writtenby:anhty9le


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        P = 1
        n = len(nums)
        k = 0

        for i in range(n):
            P *= nums[i]

            if P == 0:
                k = i
                P = 1

                for i in range(k):
                    P *= nums[i]

                for j in range(k + 1, n):
                    P *= nums[j]

                arr = [0 for i in range(n)]
                arr[k] = P

                return arr
        arr = []

        for i in range(n):
            arr.append(P / nums[i])

        return arr
