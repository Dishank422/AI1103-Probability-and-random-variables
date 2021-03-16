from random import randint

sim_len = 100000

count = sim_len
for i in range(sim_len):
    X = randint(1, 100)
    if (X % 2 == 0) or (X % 3 == 0) or (X % 5 == 0):
        count -= 1

required_probability = count / sim_len
print("Required probability = ", required_probability)
print("which is approximately equal to 0.26(theoritical value)")
