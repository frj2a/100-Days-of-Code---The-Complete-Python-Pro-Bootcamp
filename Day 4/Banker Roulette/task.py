import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option #1
friend = random.randint(0, len(friends)-1)
print (friends[friend])

# Option #2
print(random.choice(friends))