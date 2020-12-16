from gfg import Block
blockchain=[]
genesisblock=Block("chancellor on the...",["saoshi","maria","hi"])
secondblock=Block(genesisblock.blockhash,["niyas","fayas"])
thirdblock=Block(secondblock.blockhash,["nothing"])
print("Blockhash: genisis block")
print(genesisblock.blockhash)
print(secondblock.blockhash)
print(thirdblock.blockhash)