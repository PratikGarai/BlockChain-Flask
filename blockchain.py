class BlockChain(object):

    def __init__(self, *args, **kwargs):
        self.chain = []
        self.current_transaction = []

    
    def new_block(self):
        # Create a new block and add to chain
        pass
    

    def new_transaction(self):
        # Add a new transaction to the current transaction list
        pass

    
    @staticmethod
    def hash(block):
        # Calculate Hash of a block
        pass
    

    @property
    def last_block():
        # Return the last block in the chain
        pass
