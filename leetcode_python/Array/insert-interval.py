"""

Given a set of non-overlapping intervals, 
insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Example 3:

Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]

Example 4:

Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]

Example 5:

Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= intervals[i][0] <= intervals[i][1] <= 105
intervals is sorted by intervals[i][0] in ascending order.
newInterval.length == 2
0 <= newInterval[0] <= newInterval[1] <= 105

"""

# V0
# IDEA : compare merged[-1][1]. interval[0]
# https://leetcode.com/problems/insert-interval/discuss/1236101/Python3-Easy-to-Understand-Solution
### NOTE : there are only 2 cases
# case 1) no overlap -> append interval directly
# case 2) overlap -> MODIFY 2nd element in last merged interval with the bigger index
class Solution:
    def insert(self, intervals, newInterval):
        ### NOTE THIS TRICK!!! : APPEND newInterval to intervals
        intervals.append(newInterval)
        # need to sort first (by 1st element)
        intervals.sort(key=lambda x:x[0])
        merged = []
        for interval in intervals:
            ### NOTE this condition
            # if not merged : append directly
            # if merged[-1][1] < interval[0] : means no overlap : append directly as well
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                ### NOTE this op, if there is overlap, we ONLY modify the 2nd element in last interval with BIGGER digit
                merged[-1][1]= max(merged[-1][1],interval[1])
        return merged

# V1
class Solution:
    def insert(self, intervals, newInterval):
        res= []
        intervals.append(newInterval)
        intervals= sorted(intervals)
        cur_interval = intervals[0]
        for i in range(1, len(intervals)):
            if cur_interval[1]>=intervals[i][0]:
                cur_interval[1]= max(cur_interval[1], intervals[i][1])
            else:
                res.append(cur_interval)
                cur_interval=intervals[i]
        res.append(cur_interval)
        return res

# V1'
# https://leetcode.com/problems/insert-interval/discuss/21667/Python-solution-with-detailed-explanation
# IDEA
# First merge the newInterval with the existing sorted list. Use the standard code to merge two sorted lists.
# Then simply run the algorithm to merge a sorted interval list. https://discuss.leetcode.com/topic/75108/python-solution-with-detailed-explanation
class Solution(object):
    def merge(self, intervals):
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            i1, i2 = result[-1], intervals[i]
            if i2[0] > i1[1]:
                result.append(i2)
            elif i2[1] >= i1[1]:
                i1[1] = i2[1]
        return result

    def insert(self, intervals, newInterval):
        result = []
        l1, l2 = intervals, [newInterval]
        i, j = 0, 0
        while i < len(l1) or j < len(l2):
            if i == len(l1):
                result.append(l2[j])
                j += 1
            elif j == len(l2):
                result.append(l1[i])
                i += 1
            elif l1[i][0] <= l2[j][0]:
                result.append(l1[i])
                i += 1
            else:
                result.append(l2[j])
                j += 1
        return self.merge(result)