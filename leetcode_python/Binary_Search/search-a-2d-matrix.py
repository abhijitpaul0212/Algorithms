"""

74. Search a 2D Matrix
Medium


Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

"""

# V0 
# IDEA : MATRIX IN ORDER + BRUTE FORCE
# Space: O(1)
# Time:  O(m+n) # worst case
class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False        
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target: 
                return True
            elif matrix[row][col] < target: 
                row += 1
            elif matrix[row][col] > target: 
                col -= 1
        return False

# V0'
# IDEA : DFS
class Solution(object):
    def searchMatrix(self, matrix, target):
        def dfs(matrix, target, x, y):
            if matrix[y][x] == target:
                res.append(True)
            matrix[y][x] = "#"
            moves = [[0,1],[0,-1],[1,0],[-1,0]]
            for move in moves:
                _x = x + move[1]
                _y = y + move[0]
                #print ("_x = " + str(_x) + " _y = " + str(_y))
                if 0 <= _x < w and 0 <= _y < l:
                    if matrix[_y][_x] != "#":
                        dfs(matrix, target, _x, _y)

        if not matrix:
            return False
        l = len(matrix)
        w = len(matrix[0])
        res = []
        dfs(matrix, target, 0, 0)
        return True in res

# V0'
# IDEA : BINARY SEARCH
# Space: O(1)
# Time:  O(logm + logn)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n
        while left < right:
            mid = left + (right - left) / 2
            if matrix[int(mid / n)][int(mid % n)]>= target:
                right = mid
            else:
                left = mid + 1
        return left < m * n and matrix[int(left / n)][int(left % n)] == target

# V1
# https://leetcode.com/problems/search-a-2d-matrix/discuss/351404/Python-Simple-Solution
class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False

        row, col = 0, len(matrix[0]) - 1
        
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target: return True
            elif matrix[row][col] < target: row += 1
            elif matrix[row][col] > target: col -= 1
        
        return False

### Test case
s=Solution()
assert s.searchMatrix([[1,2,3],[4,5,6],[7,8,9]], 9) == True
assert s.searchMatrix([[1,2,3],[4,5,6],[7,8,9]], 1) == True
assert s.searchMatrix([[1,2,3],[4,5,6],[7,8,9]], 99) == False
assert s.searchMatrix([[]], 0) == False
assert s.searchMatrix([[]], 100) == False
assert s.searchMatrix([], 100) == False
assert s.searchMatrix([[-1,3,4,-4]], -1) == False
assert s.searchMatrix([[_ for _ in range(3)] for _ in range(4)], -1) == False
assert s.searchMatrix([[_ for _ in range(3)] for _ in range(4)], 2) == True
assert s.searchMatrix([[_ for _ in range(99)] for _ in range(999)], 2) == True

# V1'
# https://leetcode.com/problems/search-a-2d-matrix/discuss/592696/python-super-easy
# IDEA : BRUTE FORCE
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for x in matrix:
            if target in x:
                return True
        return False

# V1''
# https://blog.csdn.net/fuxuemingzhu/article/details/79459314
# https://blog.csdn.net/fuxuemingzhu/article/details/79459200
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, cols - 1
        while True:
            if row < rows and col >= 0:
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] < target:
                    row += 1
                else:
                    col -= 1
            else:
                return False

# V1' 
# https://blog.csdn.net/fuxuemingzhu/article/details/79459314
# https://blog.csdn.net/fuxuemingzhu/article/details/79459200
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return any(target in row for row in matrix)
        
# V2 
# IDEA : BINARY SEARCH
# Space: O(1)
# Time:  O(logm + logn)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n
        while left < right:
            mid = left + (right - left) / 2
            if matrix[int(mid / n)][int(mid % n)]>= target:
                right = mid
            else:
                left = mid + 1
        return left < m * n and matrix[int(left / n)][int(left % n)] == target