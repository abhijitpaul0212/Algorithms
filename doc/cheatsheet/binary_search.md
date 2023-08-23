# Binary Search
- Find a value (k) from a `sorted search space` with two pointers
    - Not really NEED to "all sorted", `partial sorted`, `rotated sorted` is possible as well
- Steps
    - step 1) Define boundary variables (e.g. left, right) that can `include all possible cases`
    - step 2) Define returned values
    - step 3) Define exit condition
- Scenario
    - find a value from sorted array
    -  if there is kind of monotonicity, for example, if condition(k) is True then condition(k + 1) is True, then we can consider binary search

- Ref
    - bisect : check [python_trick.md](https://github.com/yennanliu/CS_basics/blob/master/doc/cheatsheet/python_trick.md) : can get idx, and keep array sorted, when there is a element inserted


## 0) Concept  

### 0-1) Types

- Types
    - Find `LEFT` boundary
        - LC 367 Valid Perfect Square
        - LC 875 Koko Eating Bananas
        - the condition are nearly the same, ONLY difference : return `LEFT`
        ```python
        # python
        while r >= l:
            mid = (l + r) // 2
            if mid < target:
                r = mid - 1
            else:
                l = mid + 1
        return l
        ```

    - Find `RIGHT` boundary
        - the condition are nearly the same, ONLY difference : return `RIGHT`
        ```python
        # python
        while r >= l:
            mid = (l + r) // 2
            if mid < target:
                r = mid - 1
            else:
                l = mid + 1
        return r
        ```
    - `Recursive` binary search
        - Garena/test1.py
    - Search in Rotated Sorted Array
        - LC 033
    - Search in 2D array
        - LC 74
    - Find min in Rotation array
        - LC 153
            - Compare mid with left, right

- Algorithm
    - binary search
    - sliding window
    - recursive

- Data structure
    - Array
    - Linked list
    - dict

### 0-2) Pattern
 - [Binary-Search-101-The-Ultimate-Binary-Search-Handbook](https://leetcode.com/problems/binary-search/discuss/423162/Binary-Search-101-The-Ultimate-Binary-Search-Handbook)
- [py powerful-ultimate-binary-search-template-solved-many-problems](https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems) : TODO : add above to cheatsheet
   
#### 0-2-0) Binary search
```python
# python
# basic
def binary_search(nums, target):
    l = 0
    r = len(nums) - 1
    """
    NOTE : WE ALWALYS USE CLOSED boundary (for logic unifying)
        -> e.g. while l <= r
        -> [l, r] 
    """ 
    while l <= r:
        mid = l + (r-l)//2
        if nums[mid] == target:
            return mid 
        elif nums[mid] < target:
            ### NOTE this
            l = mid+1
        else:
            ### NOTE this
            r = mid-1 
    return -1
```

```c++
// c++
int binarySearch(int[] nums, int target) {
    int left = 0, right = ...;

    while(...) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            ...
        } else if (nums[mid] < target) {
            left = ...
        } else if (nums[mid] > target) {
            right = ...
        }
    }
    return ...;
}
```

#### 0-2-1) Binary search on `LEFT` boundary
```python
# python
def binary_search_left_boundary(nums, target):
    l = 0
    r = len(nums) - 1
    """
    NOTE : WE ALWALYS USE CLOSED boundary (for logic unifying)
        -> e.g. while l <= r
        -> [l, r] 
    """ 
    while l <= r:
        mid = l + (r-l)//2
        # DO NOT RETURN !!!, BUT REDUCE RIGHT BOUNDARY FOR FOCUSING ON LEFT BOUNDARY
        if nums[mid] == target:
            r = mid - 1 
        elif nums[mid] < target:
            ### NOTE this
            l = mid + 1
        else:
            ### NOTE this
            r = mid - 1
    # finally check if it will be OUT OF LEFT boundary
    if l >= len(nums) or nums[l] != target:
        return - 1
    return l
```

```java
// java
int left_bound(int[] nums, int target){
    int left = 0;
    int right = nums.length - 1;
    // NOTE : WE ALWALYS USE CLOSED boundary (for logic unifying)
    //       -> e.g. while l <= r
    //        -> [l, r]  
    while (left <= right){
        int mid = left + (right - mid) / 2;
        if (num[mid] < target){
            left = mid + 1;
        }else if (nums[mid] > target){
            right = mid - 1;
        }else if (nums[mid] == target){
            // DO NOT RETURN !!!, BUT REDUCE RIGHT BOUNDARY FOR FOCUSING ON LEFT BOUNDARY
            right = mid - 1;
        }
    }
    // finally check if it will be OUT OF LEFT boundary
    if (left >= nums.length || nums[left] != target){
        return -1;
    return left;
    }
}
```

#### 0-2-2) Binary search on `RIGHT` boundary
```python
# python
def binary_search_right_boundary(nums, target):
    l = 0
    r = len(nums) - 1
    """
    NOTE : WE ALWALYS USE CLOSED boundary (for logic unifying)
        -> e.g. while l <= r
        -> [l, r] 
    """ 
    while l <= r:
        mid = l + (r-l)//2
        # DO NOT RETURN !!!, BUT REDUCE LEFT BOUNDARY FOR FOCUSING ON RIGHT BOUNDARY
        if nums[mid] == target:
            l = mid + 1 
        elif nums[mid] < target:
            ### NOTE this
            l = mid + 1
        else:
            ### NOTE this
            r = mid - 1
    # finally check if it will be OUT OF RIGHT boundary
    if r < 0 or nums[r] != target:
        return - 1
    return r
```

```java
// java
int right_bound(int[] nums, int target){
    int left = 0;
    int right = nums.length - 1;
    // NOTE : WE ALWALYS USE CLOSED boundary (for logic unifying)
    //       -> e.g. while l <= r
    //        -> [l, r]  
    while (left <= right){
        int mid = left + (right - mid) / 2;
        if (num[mid] < target){
            left = mid + 1;
        }else if (nums[mid] > target){
            right = mid - 1;
        }else if (nums[mid] == target){
            // DO NOT RETURN !!!, BUT REDUCE LEFT BOUNDARY FOR FOCUSING ON RIGHT BOUNDARY
            left = mid + 1;
        }
    }
    // finally check if it will be OUT OF RIGHT boundary
    if (right < 0 || nums[right] != target){
        return -1;
    return right;
    }
}
```

## 1) General form

## 2) LC Example

### 2-0) Search in Rotated Sorted Array
```python
# LC 033. Search in Rotated Sorted Array
# LC 081. Search in Rotated Sorted Array II
# V0
# IDEA : BINARY SEARCH
#        -> CHECK WHICH PART IS ORDERING
#        -> CHECK IF TARGET IS IN WHICH PART
# CASES :
#  1) if mid is on the right of pivot -> array[mid:] is ordering
#     -> check if mid in on the left or right on mid
#     -> binary search on left or right sub array
#  2) if mid in on the left of pivot  -> array[:mid] is ordering
#     -> check if mid in on the left or right on mid
#     -> binary search on left or right sub array
### NOTE : THE NESTED IF ELSE CONDITION 
class Solution(object):
    def search(self, nums, target):
        if not nums: return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            #---------------------------------------------
            # Case 1 :  nums[mid:right] is ordering
            #---------------------------------------------
            # all we need to do is : 1) check if target is within mid - right, and move the left or right pointer
            if nums[mid] < nums[right]:
                # mind NOT use (" nums[mid] < target <= nums[right]")
                # mind the "<="
                if target > nums[mid] and target <= nums[right]: # check the relationship with target, which is different from the default binary search
                    left = mid + 1
                else:
                    right = mid - 1
            #---------------------------------------------
            # Case 2 :  nums[left:mid] is ordering
            #---------------------------------------------
            # all we need to do is : 1) check if target is within left - mid, and move the left or right pointer
            else:
                # # mind NOT use (" nums[left] <= target < nums[mid]")
                # mind the "<="
                if target < nums[mid] and target >= nums[left]:  # check the relationship with target, which is different from the default binary search
                    right = mid - 1
                else:
                    left = mid + 1
        return -1     
```

```java
// java
// LC 33
// V3
// IDEA : One Binary Search
// https://leetcode.com/problems/search-in-rotated-sorted-array/editorial/
public int search_4(int[] nums, int target) {
    int n = nums.length;
    int left = 0, right = n - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        // Case 1: find target
        if (nums[mid] == target) {
            return mid;
        }

        // Case 2: subarray on mid's left is sorted
        else if (nums[mid] >= nums[left]) {
            if (target >= nums[left] && target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        // Case 3: subarray on mid's right is sorted
        else {
            if (target <= nums[right] && target > nums[mid]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }

    return -1;
}
```

### 2-1) Two Sum II - Input array is sorted
- (For loop binary search)
```python
# 167 Two Sum II - Input array is sorted
class Solution(object):
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1
```

### 2-2) Find Peak Element
-  (recursive/iterative binary search)
```python
# LC 162 Find Peak Element, LC 852 Peak Index in a Mountain Array
# V0'
# IDEA : RECURSIVE BINARY SEARCH
class Solution(object):
    def findPeakElement(self, nums):

        def help(nums, l, r):
            if l == r:
                return l
            mid = l + (r - l) // 2
            if (nums[mid] > nums[mid+1]):
                return help(nums, l, mid) # r = mid
            return help(nums, mid+1, r) # l = mid + 1
            
        return help(nums, 0, len(nums)-1)
```

```java
// java
// LC 162
// V2
// IDEA: RECURSIVE BINARY SEARCH
// https://leetcode.com/problems/find-peak-element/editorial/
    // NOTE : ONLY have to compare index i with index i + 1 (its right element)
    //        ; otherwise, i-1 already returned as answer
    public int findPeakElement_2(int[] nums) {
        return search(nums, 0, nums.length - 1);
    }
    public int search(int[] nums, int l, int r) {
        if (l == r)
            return l;
        int mid = (l + r) / 2;
        if (nums[mid] > nums[mid + 1])
            return search(nums, l, mid);
        return search(nums, mid + 1, r);
    }

// V3
// IDEA: ITERATIVE BINARY SEARCH
// https://leetcode.com/problems/find-peak-element/editorial/
    public int findPeakElement_3(int[] nums) {
        int l = 0, r = nums.length - 1;
        while (l < r) {
            int mid = (l + r) / 2;
            if (nums[mid] > nums[mid + 1])
                r = mid;
            else
                l = mid + 1;
        }
        return l;
    }
```

### 2-3) Valid Perfect Square
```python
# 367 Valid Perfect Square, LC 69 Sqrt(x)
# V0'
# IDEA : BINARY SEARCH
class Solution(object):
    def isPerfectSquare(self, num):
        left, right = 0, num
        while left <= right:
            ### NOTE : there is NO mid * mid == num condition
            mid = (left + right) / 2
            if mid * mid >= num:
                right = mid - 1
            else:
                left = mid + 1
        ### NOTE this
        return left * left == num
```

### 2-4) Minimum Size Subarray Sum
```python
# LC 209 Minimum Size Subarray Sum
### NOTE : there is also sliding window approach
# V1' 
# http://bookshadow.com/weblog/2015/05/12/leetcode-minimum-size-subarray-sum/
# IDEA : BINARY SEARCH 
class Solution:
    def minSubArrayLen(self, s, nums):
        size = len(nums)
        left, right = 0, size
        bestAns = 0
        while left <= right:
            mid = (left + right) / 2
            if self.solve(mid, s, nums):
                bestAns = mid
                right = mid - 1
            else:
                left = mid + 1
        return bestAns

    def solve(self, l, s, nums):
        sums = 0
        for x in range(len(nums)):
            sums += nums[x]
            if x >= l:
                sums -= nums[x - l]
            if sums >= s:
                return True
        return False
```

### 2-5) First Bad Version
```python
# LC 278
# V0
# IDEA : binary search
class Solution(object):
    def firstBadVersion(self, n):
        left = 1 
        right = n
        while right > left + 1:
            mid = (left + right)//2
            if SVNRepo.isBadVersion(mid):
                end = mid 
            else:
                left = mid 
        if SVNRepo.isBadVersion(left):
            return left
        return right 
```

### 2-6) Search Insert Position
```python
# LC 035 Search Insert Position
# V1' 
# https://blog.csdn.net/fuxuemingzhu/article/details/70738108
class Solution(object):
    def searchInsert(self, nums, target):
        N = len(nums)
        left, right = 0, N #[left, right)
        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left
```

### 2-7) Capacity To Ship Packages Within D Days
```python
# LC 1011
# V1
# IDEA : BINARY SEARCH
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/390359/Simple-Python-Binary-Search
# V0
# IDEA : BINARY SEARCH
class Solution(object):
     def shipWithinDays(self, weights, D):
            """
            NOTE !!!
                -> for this help func,
                -> we ONLY need to check weights can split by offered max_wgt
                -> so the return val is boolean (True or False)
            """
            # help func
            def cannot_split(weights, D, max_wgt):
                s = 0
                days = 1
                for w in weights:
                    s += w
                    if s > max_wgt:
                        s = w
                        days += 1
                return days > D

            """
            NOTE this !!!
                -> for l, we use max(weights)
                -> for r, we use sum(weights)
            """
            l = max(weights)
            r = sum(weights)
            while l <= r:
                mid = l + (r - l) // 2
                if cannot_split(weights, D, mid):
                    l = mid + 1
                else:
                    r = mid - 1
            return l
```

### 2-8) Split Array Largest Sum (Hard)
```python
# LC 410 Split Array Largest Sum [Hard]
```

### 2-9) Koko Eating Bananas
```python
# LC 875. Koko Eating Bananas
# V1
# IDEA : BINARY SEARCH
# https://leetcode.com/problems/koko-eating-bananas/solution/
class Solution:
    def minEatingSpeed(self, piles, h):  
        # Initalize the left and right boundaries     
        left = 1
        right = max(piles)
        
        while left < right:
            # Get the middle index between left and right boundary indexes.
            # hour_spent stands for the total hour Koko spends.
            middle = (left + right) // 2            
            hour_spent = 0
            
            # Iterate over the piles and calculate hour_spent.
            # We increase the hour_spent by ceil(pile / middle)
            for pile in piles:
                # python ceil : https://www.runoob.com/python/func-number-ceil.html
                hour_spent += math.ceil(pile / middle)
            
            # Check if middle is a workable speed, and cut the search space by half.
            if hour_spent <= h:
                right = middle
            else:
                left = middle + 1
        
        # Once the left and right boundaries coincide, we find the target value,
        # that is, the minimum workable eating speed.
        return right

# V1' 
# https://blog.csdn.net/fuxuemingzhu/article/details/82716042
# IDEA : BINARY SEARCH 
class Solution:
    def minEatingSpeed(self, piles, H):
        minSpeed, maxSpeed = 1, max(piles)
        while minSpeed <= maxSpeed:
            speed = minSpeed + (maxSpeed - minSpeed) // 2
            hour = 0
            for pile in piles:
                hour += math.ceil(pile / speed)
            if hour <= H:
                maxSpeed = speed - 1
            else:
                minSpeed = speed + 1
        return minSpeed
```

```java
// java
// LC 875

// V0
// IDEA : BINARY SEARCH (close boundary)
public int minEatingSpeed(int[] piles, int h) {

    if (piles.length == 0 || piles.equals(null)){
        return 0;
    }

    int l = 1; //Arrays.stream(piles).min().getAsInt();
    int r = Arrays.stream(piles).max().getAsInt();

    while (r >= l){
        int mid = (l + r) / 2;
        int _hour = getCompleteTime(piles, mid);
        if (_hour <= h){
            r = mid - 1;
        }else{
            l = mid + 1;
        }
    }

    return l;
}
```

### 2-10) Find K Closest Elements
```python
# LC 658. Find K Closest Elements
# V1'
# https://blog.csdn.net/fuxuemingzhu/article/details/82968136
# IDEA : TWO POINTERS 
class Solution(object):
    def findClosestElements(self, arr, k, x):
        # since the array already sorted, arr[-1] must be the biggest one,
        # while arr[0] is the smallest one
        # so if the distance within arr[-1],  x >  arr[0],  x
        # then remove the arr[-1] since we want to keep k elements with smaller distance,
        # and vice versa (remove arr[0]) 
        while len(arr) > k:
            if x - arr[0] <= arr[-1] - x:
                arr.pop()
            else:
                arr.pop(0)
        return arr
```

### 2-11) Sqrt(x)
```python
# LC 069 Sqrt(x)
# V0
# IDEA : binary search
class Solution(object):
    def mySqrt(self, x):
        # edge case
        if not x or x <= 0:
            return 0
        if x == 1:
            return 1
        l = 0
        r = x-1
        while r >= l:
            mid = l + (r-l)//2
            #print ("l = " + str(l) + " r = " + str(r) + " mid = " + str(mid))
            sq = mid** 2
            if sq == x:
                return mid
            elif sq < x:
                if (mid+1)**2 > x:
                    return mid
                l = mid + 1
            else:
                r = mid - 1

# V0
# IDEA : binary search
class Solution(object):
    def mySqrt(self, num):
        if num <= 1:
            return num
        l = 0
        r = num - 1
        while r >= l:
            mid = l + (r - l) // 2
            if mid * mid == num:
                return mid
            elif mid * mid > num:
                r = mid - 1
            else:
                l = mid + 1
        return l if l * l < num else l - 1
```

### 2-12) Find First and Last Position of Element in Sorted Array
```python
# 34. Find First and Last Position of Element in Sorted Array
# V0
# IDEA : BINARY SEARCH
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def search(x):
            lo, hi = 0, len(nums)           
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid+1
                else:
                    hi = mid                    
            return lo
        
        lo = search(target)
        hi = search(target+1)-1
        
        if lo <= hi:
            return [lo, hi]
                
        return [-1, -1]
```

### 2-13) Search a 2D Matrix
```java
// java
// LC 74
// V1
// IDEA : BINARY SEARCH + FLATTEN MATRIX
// https://leetcode.com/problems/search-a-2d-matrix/editorial/
public boolean searchMatrix_2(int[][] matrix, int target) {
    int m = matrix.length;
    if (m == 0)
        return false;
    int n = matrix[0].length;

    // binary search
    /** NOTE !!! FLATTEN MATRIX */
    int left = 0, right = m * n - 1;
    int pivotIdx, pivotElement;
    while (left <= right) {
        pivotIdx = (left + right) / 2;
        /** NOTE !!! TRICK HERE :
         *
         *   pivotIdx / n : y index
         *   pivotIdx % n : x index
         */
        pivotElement = matrix[pivotIdx / n][pivotIdx % n];
        if (target == pivotElement)
            return true;
        else {
            if (target < pivotElement)
                right = pivotIdx - 1;
            else
                left = pivotIdx + 1;
        }
    }
    return false;
}
```

### 2-14) Find Minimum in Rotated Sorted Array
```java
// java
// LC 153
// V0
// IDEA : BINARY SEARCH (CLOSED BOUNDARY)
// NOTE !!! the turing point (rotation point)
//          is ALWAYS the area that min element located (may at at i, i+1, i-1 place)
public int findMin(int[] nums) {

    if (nums.length == 0 || nums.equals(null)){
        return 0;
    }

    // already in ascending order
    if (nums[0] < nums[nums.length - 1]){
        return nums[0];
    }

    if (nums.length == 1){
        return nums[0];
    }

    // binary search
    int l = 0;
    int r = nums.length - 1;
    /** NOTE !!! here : r >= l (closed boundary) */
    while (r >= l){
        int mid = (l + r) / 2;
        /** NOTE !!! we found turing point, and it's the minimum element  (idx = mid + 1) */
        if (nums[mid] > nums[mid+1]){
            return nums[mid+1];
       /** NOTE !!! we found turing point, and it's the minimum element (idx = mid -1) */
        }else if (nums[mid-1] > nums[mid]){
            return nums[mid];
        /** NOTE !!! compare mid with left, and this means left sub array is ascending order,
         *           so minimum element MUST in right sub array
         */
        }else if (nums[mid] > nums[l]){
            l = mid + 1;
        /** NOTE !!! compare mid with left, and this means right sub array is ascending order,
        *            so minimum element MUST in left sub array
        */
        }else{
            r = mid - 1;
        }
    }

    return nums[l];
}


// V1
// IDEA : BINARY SEARCH (CLOSED BOUNDARY)
// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/editorial/
public int findMin_3(int[] nums) {
    // If the list has just one element then return that element.
    if (nums.length == 1) {
        return nums[0];
    }

    // initializing left and right pointers.
    int left = 0, right = nums.length - 1;

    // if the last element is greater than the first element then there is no
    // rotation.
    // e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
    // Hence the smallest element is first element. A[0]
    if (nums[right] > nums[0]) {
        return nums[0];
    }

    // Binary search way
    while (right >= left) {
        // Find the mid element
        int mid = left + (right - left) / 2;

        // if the mid element is greater than its next element then mid+1 element is the
        // smallest
        // This point would be the point of change. From higher to lower value.
        if (nums[mid] > nums[mid + 1]) {
            return nums[mid + 1];
        }

        // if the mid element is lesser than its previous element then mid element is
        // the smallest
        if (nums[mid - 1] > nums[mid]) {
            return nums[mid];
        }

        // if the mid elements value is greater than the 0th element this means
        // the least value is still somewhere to the right as we are still dealing with
        // elements
        // greater than nums[0]
        if (nums[mid] > nums[0]) {
            left = mid + 1;
        } else {
            // if nums[0] is greater than the mid value then this means the smallest value
            // is somewhere to
            // the left
            right = mid - 1;
        }
    }
    return Integer.MAX_VALUE;
}
```