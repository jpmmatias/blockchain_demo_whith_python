from Chain import Chain

chain = Chain(20)

for i in range(5):
  chain.add_to_pool(str(i))
  chain.mine()
