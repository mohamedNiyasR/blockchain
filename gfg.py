import hashlib

class Block:
    def __init__(self,previoushash,transaction):
        self.transaction=transaction
        self.previoushash=previoushash
        stringtohash="".join(transaction) + previoushash
        self.blockhash=hashlib.sha256(stringtohash.encode()).hexdigest()