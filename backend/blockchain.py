import time
import json
import hashlib

class BlockChain(object):

    def __init__(self, *args, **kwargs):
        self.chain = []
        self.current_transactions = []
        self.hash_difficulty = 4
        self.hash_suffix = "0"*self.hash_difficulty

        # adding genesis
        self.new_block(100, 1)
        
    
    # create a new block and  add to chain
    def new_block(self, proof, previous_hash = None):
        block = {
                'index' : len(self.chain)+1,
                'timestamp' : time.time_ns(),
                'transactions' : self.current_transactions,
                'proof' : proof,
                'previous_hash' : previous_hash
        }

        self.current_transactions=  []
        self.chain.append(block)
        return block

    
    # Add a new transaction to the current transaction list
    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender' : sender,
            'recipient' : recipient,
            'amount' : amount
            })

        return self.last_block['index']+1
    

    # Calculate Hash of a block
    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(block_string).hexdigest()


    # Return the last block in the chain
    @property
    def last_block(self):
        return self.chain[-1]


    # proof of work impolementation
    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof
    
    # prrof of work checker function
    def valid_proof(self, last_proof, proof):
        guess = str.encode(str(last_proof)+str(proof))
        guesshash = hashlib.sha256(guess).hexdigest()
        return guesshash[:self.hash_difficulty]==self.hash_suffix
