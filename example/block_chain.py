
class BlockChain(object):
    def __init__(self):
        self.head = None
        self.blocks = {}

    def add_block(self,new_block):
        prev_hash = self.head.hash(self.head.nonce) if self.head else None
        new_block.prev_hash = prev_hash
        self.blocks[new_block.ident] = {
            'block':new_block,
            'prev_hash':prev_hash,
            'prev':self.head
        }
        self.head = new_block

    def __repr__(self):
        num_exist_blks = len(self.blocks)
        return 'BlockChain<{} Blocks,Head:{},Head nonce:{}>'.format(
            num_exist_blks,
            self.head.ident if self.head else None,
            self.head.nonce if self.head else None
        )



