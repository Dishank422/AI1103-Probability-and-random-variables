from scipy.stats import expon, gamma

sim_len = 1000000
count = 0

Y1 = expon.rvs(size = sim_len)
Y2 = expon.rvs(size = sim_len)
Y3 = expon.rvs(size = sim_len)
Y4 = expon.rvs(size = sim_len)
Y5 = expon.rvs(size = sim_len)
Y6 = expon.rvs(size = sim_len)
Y7 = expon.rvs(size = sim_len)
Y8 = expon.rvs(size = sim_len)
Y9 = expon.rvs(size = sim_len)
Y10 = expon.rvs(size = sim_len)
Y11 = expon.rvs(size = sim_len)
Y12 = expon.rvs(size = sim_len)

X1 = gamma.rvs(a = 2, size = sim_len)
X2 = gamma.rvs(a = 2, size = sim_len)
X3 = gamma.rvs(a = 2, size = sim_len)

for i in range(sim_len):
    if (min(Y1[i],Y2[i],Y3[i],Y4[i],Y5[i],Y6[i],Y7[i],Y8[i],Y9[i],Y10[i],X1[i]+Y11[i]) > X1[i]+X2[i]) and (min(Y1[i],Y2[i],Y3[i],Y4[i],Y5[i],Y6[i],Y7[i],Y8[i],Y9[i],Y10[i],X1[i]+Y11[i],X1[i]+X2[i]+Y12[i]) < X1[i]+X2[i]+X3[i]):
        count += 1

print("Experimental probability = ", count / sim_len)
print("which is approximately equal to 5.7e-05(theoritical value)")                                                                   
