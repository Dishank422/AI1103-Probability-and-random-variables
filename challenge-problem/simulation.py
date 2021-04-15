from scipy.stats import cauchy
import matplotlib.pyplot as plt

sim_len = 1000000

X = cauchy.rvs(size = sim_len)
Y = cauchy.rvs(size = sim_len)
Z = []

for i in range(sim_len):
    if -100<X[i] + Y[i]<100:
        Z.append((X[i]+Y[i])/3)

plt.hist(Z, bins = 100)
plt.show()
