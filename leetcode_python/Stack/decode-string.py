"""

394. Decode String
Medium

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].

"""

# V0
# IDEA : STACK
# NOTE : treat before cases separately
#        1) isdigit
#        2) isalpha
#        3) "["
#        4) "]"
# and define num = 0 for dealing with "100a[b]", "10abc" cases
class Solution:
    def decodeString(self, s):
        num = 0
        string = ''
        stack = []
        """
        NOTE : we deal with 4 cases
            1) digit
            2) "["
            3) alphabet
            4) "]"

        NOTE : 
            we use pre_num, pre_string for dealing with previous result
        """
        for c in s:
            # case 1) : digit
            if c.isdigit():
                num = num*10 + int(c)
            # case 2) : "["
            elif c == "[":
                stack.append(string)
                stack.append(num)
                string = ''
                num = 0
            # case 3) : alphabet
            elif c.isalpha():
                string += c
            # case 4) "]"
            elif c == ']':
                pre_num = stack.pop()
                pre_string = stack.pop()
                string = pre_string + pre_num * string
        return string

# V1
# https://leetcode.com/problems/decode-string/discuss/378711/Easy-understand-python-solution-88-beat
# IDEA : STACK 
# IDEA :
#  -> When meet '[' append the previous num and string to stack, 
#  -> when meet the ']' pop the previous num and string to calculate. 
#  -> Notice the num*10 + num is for some case like "100[leetcode]" that num is greater than 10.
class Solution:
    def decodeString(self, s):
        num = 0
        string = ''
        stack = []
        for c in s:
            if c.isdigit():
                ### NOTICE HERE 
                # num = num*10 + int(c) is for the greater than 10 cases
                # e.g. 
                # input = 100 
                # -> when idx=0
                #  -> num=0*10 + 1
                # -> when idx=1
                #  -> num += 1*10 + 0
                # -> when idx=2
                #  -> num += 10*10 + 0 
                # -> so num = 100 
                num = num*10 + int(c)
            elif c == "[":
                # when c == "["
                # then cache string and num
                # and init string, num again
                stack.append(string)
                stack.append(num)
                string = ''
                num = 0
            elif c.isalpha():
                string += c
            elif c == ']':
                # when c == ']',
                # pop pre num, pre string 
                # do pre_string + pre_num and add it back to string  
                pre_num = stack.pop()
                pre_string = stack.pop()
                string = pre_string + pre_num * string
        return string

### Test case
s=Solution()
assert s.decodeString("3[a]2[bc]")=="aaabcbc"
assert s.decodeString("3[a2[c]]")=="accaccacc"
assert s.decodeString("2[abc]3[cd]ef")=="abcabccdcdcdef"
assert s.decodeString("")==""
assert s.decodeString("[]")==""
assert s.decodeString("a")=="a"
assert s.decodeString("abc")=="abc"
assert s.decodeString("[[]]")==""
assert s.decodeString("[[[]]]")==""
assert s.decodeString("[[a]]")==""
assert s.decodeString("[[ab]]")==""
assert s.decodeString("[[[a]]b]")==""

# V1' 
# https://blog.csdn.net/fuxuemingzhu/article/details/79332894
# IDEA : STACK
# curstring = prestring + prenum * curstring 
# ord() is a way transforming string -> integer 
# e.g. 
# c = '3' -> ord(c) - ord('0') = 3 
# c= '9'  -> ord(c) - ord('0') = 9
# we can do that via int() as well. i.e. int('9') -> 9 
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        curnum = 0
        curstring = ''
        stack = []
        for char in s:
            if char == '[':
                stack.append(curstring)
                stack.append(curnum)
                curstring = ''
                curnum = 0
            elif char == ']':
                prenum = stack.pop()
                prestring = stack.pop()
                curstring = prestring + prenum * curstring
            elif char.isdigit():
                curnum = curnum * 10 + int(char)
            else:
                curstring += char
        return curstring

# V1''
# https://leetcode.com/problems/decode-string/discuss/163479/Python-short-and-simple-stack-solution-beats-100-with-explanation
class Solution:
      def decodeString(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == "]":
                current = ''
                while stack:
                    val = stack.pop()
                    if val ==  "[":
                        break
                    current = val + current
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num)*current)
            else:
                stack.append(s[i])
        return ''.join(stack)

# V1'''
# https://leetcode-cn.com/problems/decode-string/solution/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)            
            else:
                res += c
        return res

# V1''''
# https://yq.aliyun.com/articles/714166
class Solution:
    def decodeString(self, s: str) -> str:
        #init
        stack, res, num = [], '', 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c.isalpha():
                res += c
            elif c == '[':
                # insert into stack as tuple (res, num )
                stack.append((res, num))
                # update res and num 
                res, num = '', 0
            else:
                # if c == ']', then pop var and repeat times
                last_str, this_num = stack.pop()
                res = last_str + this_num * res
        return res

# V1''''''
# http://bookshadow.com/weblog/2016/09/04/leetcode-decode-string/
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        k = 1
        parts = collections.defaultdict(str)
        digits = collections.defaultdict(int)
        for c in s:
            if c.isdigit():
                digits[k] = digits[k] * 10 + int(c)
            elif c == '[':
                k += 1
            elif c == ']':
                parts[k - 1] += digits[k - 1] * parts[k]
                digits[k - 1] = 0
                parts[k] = ''
                k -= 1
            else:
                parts[k] += c
        return parts[1]

# V2 
# Time:  O(n)
# Space: O(n)
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        curr, nums, strs = [], [], []
        n = 0

        for c in s:
            if c.isdigit():
                n = n * 10 + ord(c) - ord('0')
            elif c == '[':
                nums.append(n)
                n = 0
                strs.append(curr)
                curr = []
            elif c == ']':
                strs[-1].extend(curr * nums.pop())
                curr = strs.pop()
            else:
                curr.append(c)

        return "".join(strs[-1]) if strs else "".join(curr)