
import block
import block_chain

def main():
    ch = block_chain.BlockChain()
    print(ch)
    for i in range(6):
        new_b = block.Block(i)
        new_b.mine()
        ch.add_block(new_b)
    print(ch)

if __name__ == "__main__":
    main()