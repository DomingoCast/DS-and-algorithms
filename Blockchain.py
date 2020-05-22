"""
Create a Blockchain 
"""
import hashlib
import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    #Define a function to create a encoded string particular to the data it has
    def calc_hash(self):
        sha = hashlib.sha256()
        string = str(self.timestamp) + str(self.previous_hash) + str(self.data)
        hash_str = string.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class BlockChain:
    def __init__(self):
        self.curr_block = self.genesis() #Create the first block and set whic block is the last one
        self.size = 0

    #Define a function to create an arbitrary block, to be the first of the chain
    def genesis(self):
        time = datetime.datetime.now()
        return(Block(time,"Genesis",0))

    #Function to link to blocks
    def add(self, data):
        time = datetime.datetime.now()
        if self.curr_block == None:
            self.curr_block = Block(time, data, 0)
            return
        previous_hash = self.curr_block.hash        #Link them by one having as previous hash
        block = Block(time,data,previous_hash)      # the hash of the former one
        self.curr_block = block                     #Make the last block, the current one

    def get_block(self):
        return self.curr_block
        

    

        
        
