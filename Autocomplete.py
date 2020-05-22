"""
Create an autocomplete feature using Tries
"""
## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        #self.char = char
        self.children = {}
        self.finished = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        #self.char = char
        self.children = {}
        self.finished = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        curr_node = self.root
        for char in prefix:
            if char not in curr_node.children:
                return
            curr_node = curr_node.children[char]
        return curr_node

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        total_sfx = [] 
        for char in self.children:
            #print('char: ', char)
            sfx  = []
            node = self.children[char]
            if node.finished: #If the word is finished, save suffix
                sfx.append(suffix + char) 
            if node.children != {}: #If it has more children, explore them
                sfx += node.suffixes(suffix + char)
            else:
                return sfx #If there are no more children, go back
            total_sfx += sfx
        return total_sfx





MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


# In[6]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');


# In[ ]:





# In[ ]:




