# Python program for insert and search 
# operation in a Trie

class TrieNode():
	# Trie node class
	def __init__(self):
		self.children = [None] *26

		# isEndOfWrod is True if node represent the end of the word
		self.isEndOfWord = False


class Trie():
	# Trie data structure class
	def __init__(self):
		self.root = self.getNode()

	def getNode(self):
		# Returns new trie noe( initialized to NULLs)
		return TrieNode()

	def _charToIndex(self, ch):
		return ord(ch)-ord('a')

	def insert(self,key):
		# If not present, inserts key into trie
		# if the key is prefix to trie mode
		pCrwal = self.root
		length = len(key)
		for level in range(length):
			index = self._charToIndex(key[level])

			# if current character is not present
			if not pCrwal.children[index]:
				pCrwal.children[index] = self.getNode()
			pCrwal = pCrwal.children[index]

		# mark last node as leaf
		pCrwal.isEndOfWord = True


	def search(self, key):
		# search key in the trie
		# return true if key presents
		# in trie, else false
		pCrwal = self.root
		length = len(key)
		for level in range(length):
			index = self._charToIndex(key[level])
			if not pCrwal.children[index]:
				return False
			pCrwal = pCrwal.children[index]

		return pCrwal != None and pCrwal.isEndOfWord


# driver function
def main():
	# Input keys (use only 'a' through 'z' and lower case)
    keys = ["the","a","there","anaswe","any",
            "by","their"]
    output = ["Absent",
              "Present"]
  
    # Trie object
    t = Trie()
  
    # Construct trie
    for key in keys:
        t.insert(key)
  
    # Search for different keys
    print("{} -> {}".format("the",output[t.search("the")]))
    print("{} -> {}".format("these",output[t.search("these")]))
    print("{} -> {}".format("their",output[t.search("their")]))
    print("{} -> {}".format("thaw",output[t.search("thaw")]))
  
if __name__ == '__main__':
    main()
