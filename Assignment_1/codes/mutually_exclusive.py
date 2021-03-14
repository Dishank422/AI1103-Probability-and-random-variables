import numpy as np

sample_size = 100000

prob_A = 0.5
prob_A_or_B = 0.6
prob_B_min = 0.0
prob_B_max = 0.5 #simce prob_B + prob_A <= 1
prob_B = (prob_B_min + prob_B_max) / 2
tolerance = 0.0001

# Let X = 1 if A = success and B = failure
# Let X = 2 if B = success and A = failure
# Let X = 3 if A = failure and B = failure
# Since A and B are mutually exclusive, P(X=1) + P(X=2) + P(X=3) = 1
# Also P(X=1) = prob_A = 0.5, P(X=2) = prob_B
# Therefore P(X=3) = 1-prob_A-prob_B = 0.5-prob_B

print("Please wait. The process takes some time")

#finding probability of B using binary search
while 1:
    count = 0
    for i in range(sample_size):
        X = np.random.choice([1, 2, 3], p = [0.5, prob_B, 0.5 - prob_B])
        if (X == 1) or (X == 2):
            count += 1
    this_iteration_prob_A_or_B = count / sample_size
    if (this_iteration_prob_A_or_B > prob_A_or_B - tolerance) and (this_iteration_prob_A_or_B < prob_A_or_B + tolerance):
        break
    elif this_iteration_prob_A_or_B > prob_A_or_B:
        prob_B_max = prob_B
        prob_B = (prob_B_min + prob_B_max) / 2
    elif this_iteration_prob_A_or_B < prob_A_or_B:
        prob_B_min = prob_B
        prob_B = (prob_B_min + prob_B_max) / 2

print("If A and B are mutually exclusive events, probability of B =", prob_B)
print("which is approximately equal to 0.1(theoritical value)")
