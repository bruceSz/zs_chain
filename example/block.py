import hashlib
import uuid

class Block(object):
    def __init__(self, data=None, previous_hash=None):
        self.ident = uuid.uuid4().hex
        self.nonce = None
        self.data = data
        self.previous_hash = previous_hash

    def hash(self,nonce=None):
        '''compute hash of chain block'''
        mess = hashlib.sha256()
        mess.update(self.ident.encode('utf-8'))
        mess.update(str(nonce).encode("utf-8"))
        mess.update(str(self.data).encode('utf-8'))
        mess.update(str(self.previous_hash).encode('utf-8'))
        return mess.hexdigest()

    def hash_is_valid(self,the_hash):
        ''' check whether the hash is valid'''
        return the_hash.startswith('00000')

    def __repr__(self):
        return 'BlockChain:{},Nonce:{}>'.format(self.hash(),self.nonce)

    def mine(self):
        cur_nonce = self.nonce or 0
        while True:
            the_hash = self.hash(nonce=cur_nonce)
            if self.hash_is_valid(the_hash):
                self.nonce = cur_nonce
                break
            else:
                cur_nonce += 1

