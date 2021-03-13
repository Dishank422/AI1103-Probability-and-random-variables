import numpy as np
from scipy.stats import bernoulli

sample_size = 100000

prob_A = 0.5
prob_A_or_B = 0.6
prob_B_min = 0.0
prob_B_max = 0.6
prob_B = (prob_B_min + prob_B_max) / 2
tolerance = 0.0001

#finding probability of B using Binary Search
while 1:
    count = sample_size
    sample_A = bernoulli.rvs(size = sample_size, p = prob_A)
    sample_B = bernoulli.rvs(size = sample_size, p = prob_B)
    for i in range(sample_size):
        if sample_A[i] == 0 and sample_B[i] == 0:
            count -= 1
    this_iteration_prob_A_or_B = count / sample_size
    if (this_iteration_prob_A_or_B > prob_A_or_B - tolerance) and (this_iteration_prob_A_or_B < prob_A_or_B + tolerance):
        break
    elif this_iteration_prob_A_or_B > prob_A_or_B:
        prob_B_max = prob_B
        prob_B = (prob_B_min + prob_B_max) / 2
    elif this_iteration_prob_A_or_B < prob_A_or_B:
        prob_B_min = prob_B
        prob_B = (prob_B_min + prob_B_max) / 2

print("If A and B are independent, probability of B =", prob_B)
print("which is approximately equal to 0.2")
