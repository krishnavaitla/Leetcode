'''
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

 

Example 1:

Input: [1,2,3,3]
Output: 3
'''



class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        k = []
        for i in A:
            if i in k:
                return i
            else:
                k.append(i)

j = Solution()
j.repeatedNTimes([1,2,3,3])
