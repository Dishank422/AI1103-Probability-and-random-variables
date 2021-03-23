from scipy.stats import norm

sim_len = 100000
count = 0

for i in range(sim_len):
    X = 0
    while 1:
        X = norm.rvs()
        if (-1 <= X < 0) or (1 <= X < 2):
            break
    if X < 0:
        count += 1

print("Experimental probability = ", count / sim_len)
print("which is approximately equal to 0.715(theoritical probability)")
