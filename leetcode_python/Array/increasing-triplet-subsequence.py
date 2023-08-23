"""

334. Increasing Triplet Subsequence
Medium

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

"""

# V0
# IDEA : MAINTAIN var first, second
#        AND GO THROUGH nums to check if there exists x (on the right hand side of a, b )
#        such that x > second > first
class Solution(object):
    def increasingTriplet(self, nums):
        """
        NOTE !!! we init first, second as POSITIVE float('inf')
        """
        first = float('inf')
        second = float('inf')
        # loop with normal ordering
        for num in nums:
            if num <= first:     # min num
                first = num
            elif num <= second:  # 2nd min num
                second = num
            else:                # 3rd min num
                return True      
        return False

# V0' 
# IDEA : MAINTAIN var a, b 
#        AND GO THROUGH nums to check if there exists x (on the right hand side of a, b )
#        such that x > a > b
# DEMO
# >>> nums = [2,1,5,0,4,6]
# >>> s= Solution()
# >>> r = s.increasingTriplet(nums)
# a = None, x = 2, b = None
# a = None, x = 1, b = 2
# a = None, x = 5, b = 1
# a = 5, x = 0, b = 1
# a = 5, x = 4, b = 0
# a = 4, x = 6, b = 0
# >>>
class Solution(object):
    def increasingTriplet(self, nums):
        ### NOTE : here we maintain a, b
        #     -> such that x > a > b (x is the element in nums)
        a = b = None
        for n in nums:
            if a is None or a >= n:    # min element (1st element) : a 
                a = n
            elif b is None or b >= n:  # 2nd min element (2nd element) : b
                b = n
            else:                      # 3rd min element (3nd element) : return Ture if this case exists
                return True
        return False

# V0'
# IDEA : brute force + 2 pointers : TLE
class Solution(object):
    def increasingTriplet(self, nums):
        # edge case
        if not nums or len(nums) < 3:
            return False
        _len = len(nums)
        # 2 pointers
        for i in range(_len-2):
            for j in range(i+1, _len-1):
                if nums[j] <= i:
                    break
                if any(x > nums[j] for x in nums[j+1:]):
                    return True
        return False

# V1
# IDEA : LINEAR SCAN
# https://leetcode.com/problems/increasing-triplet-subsequence/solution/
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = float("inf")
        second_num = float("inf")
        for n in nums:
            if n <= first_num:
                first_num = n
            elif n <= second_num:
                second_num = n
            else:
                return True
        return False

# V1'
# http://bookshadow.com/weblog/2016/02/16/leetcode-increasing-triplet-subsequence/
# IDEA :  MAINTAIN ON 2 VAR a, b (min and 2nd min)
# a IS THE CURRENT MIN ELEMENT ; 
# b IS THE ONE CLOSEST TO (NEXT TO) a and BIGGER TO a 
# PROCESS:
# STEP 1) INIT : a = b = None
# STEP 2) GO THROUGH THE ARRAY, RECORD CURRENT ELEMENT n
# STEP 3) if a is None or a >= n  ----> a = n
# STEP 3) elif b is None or b >= n ----> b = n
# STEP 3) or, return True
# STEP 4) return False 
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = b = None
        for n in nums:
            if a is None or a >= n:    # min element (1st element) : a 
                a = n
            elif b is None or b >= n:  # 2nd min element (2nd element) : b
                b = n
            else:                      # 3rd min element (3nd element) : return Ture if this case exists
                return True
        return False

# V1''
# https://blog.csdn.net/fuxuemingzhu/article/details/79826703
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first, second = float('inf'), float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False

# V2 
# Time:  O(n)
# Space: O(1)
import bisect
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min_num, a, b = float("inf"), float("inf"), float("inf")
        for c in nums:
            if min_num >= c:
                min_num = c
            elif b >= c:
                a, b = min_num, c
            else:  # a < b < c
                return True
        return False

# Time:  O(n * logk)
# Space: O(k)
# Generalization of k-uplet.
class Solution_Generalization(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def increasingKUplet(nums, k):
            inc = [float('inf')] * (k - 1)
            for num in nums:
                i = bisect.bisect_left(inc, num)
                if i >= k - 1:
                    return True
                inc[i] = num
            return k == 0
        return increasingKUplet(nums, 3)