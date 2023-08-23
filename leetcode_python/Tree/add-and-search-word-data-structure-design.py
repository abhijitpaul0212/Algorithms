"""

211. Design Add and Search Words Data Structure
Medium

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.

"""

# V0
from collections import defaultdict
class Node(object):
    def __init__(self):
        self.children = defaultdict(Node)
        self.isword = False
        
class WordDictionary(object):

    def __init__(self):
        self.root = Node()

    def addWord(self, word):
        current = self.root
        for w in word:
            _next = current.children[w]
            current = _next
        current.isword = True

    def search(self, word):
        return self.match(word, 0, self.root)
    
    def match(self, word, index, root):
        """
        NOTE : match is a helper func (for search)

          - deal with 2 cases
          -   1) word[index] != '.'
          -   2) word[index] == '.'
        """
        # note the edge cases
        if root == None:
            return False
        if index == len(word):
            return root.isword
        # CASE 1: word[index] != '.'
        if word[index] != '.':
            return root != None and self.match(word, index + 1, root.children.get(word[index]))
        # CASE 2: word[index] == '.'
        else:
            for child in root.children.values():
                if self.match(word, index + 1, child):
                    return True
        return False

# V1 
# https://blog.csdn.net/fuxuemingzhu/article/details/79390052
class Node(object):
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False
        
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        current = self.root
        for w in word:
            current = current.children[w]
        current.isword = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.match(word, 0, self.root)
    
    def match(self, word, index, root):
        if root == None:
            return False
        if index == len(word):
            return root.isword
        if word[index] != '.':
            return root != None and self.match(word, index + 1, root.children.get(word[index]))
        else:
            for child in root.children.values():
                if self.match(word, index + 1, child):
                    return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)

# V1'
# https://www.jiuzhang.com/solution/add-and-search-word-data-structure-design/#tag-highlight-lang-python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    
    def __init__(self):
        self.root = TrieNode()
        
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word =True

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        if word is None:
            return False
        return self.search_helper(self.root, word, 0)
        
    def search_helper(self, node, word, index):
        if node is None:
            return False
            
        if index >= len(word):
            return node.is_word
        
        char = word[index]
        if char != '.':
            return self.search_helper(node.children.get(char), word, index + 1)
            
        for child in node.children:
            if self.search_helper(node.children[child], word, index + 1):
                return True
                
        return False

# V1''
# https://www.jiuzhang.com/solution/add-and-search-word-data-structure-design/#tag-highlight-lang-python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    
    def __init__(self):
        self.root = TrieNode()
        
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word =True

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        if word is None:
            return False
        return self.search_helper(self.root, word, 0)
        
    def search_helper(self, node, word, index):
        if node is None:
            return False
            
        if index >= len(word):
            return node.is_word
        
        char = word[index]
        if char != '.':
            return self.search_helper(node.children.get(char), word, index + 1)
            
        for child in node.children:
            if self.search_helper(node.children[child], word, index + 1):
                return True
                
        return False

# V2 
# Time:  O(min(n, h)), per operation
# Space: O(min(n, h))
class TrieNode(object):
    # Initialize your data structure here.
    def __init__(self):
        self.is_string = False
        self.leaves = {}

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.leaves:
                curr.leaves[c] = TrieNode()
            curr = curr.leaves[c]
        curr.is_string = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self.searchHelper(word, 0, self.root)

    def searchHelper(self, word, start, curr):
        if start == len(word):
            return curr.is_string
        if word[start] in curr.leaves:
            return self.searchHelper(word, start+1, curr.leaves[word[start]])
        elif word[start] == '.':
            for c in curr.leaves:
                if self.searchHelper(word, start+1, curr.leaves[c]):
                    return True

        return False
