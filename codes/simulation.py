from scipy.stats import norm

sim_len = 10000
count = 1

for i in range(sim_len):
    X1 = norm.rvs()
    X2 = norm.rvs()
    X3 = norm.rvs()
    X4 = norm.rvs()
    if X4 == min(X1, X2, X3, X4):
        count += 1

print("Experimental probability = ", count / sim_len)
print("which is equal to 0.25(theoritical probability))")
