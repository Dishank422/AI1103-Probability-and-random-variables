import random

sim_len = 100000
count = 0

for i in range(sim_len):
    X = random.uniform(2,3)
    Y = random.uniform(1,4)
    if X <= Y:
        count += 1

print("Experimental probability = ", count / sim_len)
print("which is approximately equal to 0.5(theoritical probability)")
