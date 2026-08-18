# Q. Calculate Probabilites using Bayes' Theorem

# #Problem
# A disesase affects 1% of a population
# A test is 95% accurate for diseased individuals and 90% accurate for non-diseased individuals
# Find the probability of having the disease given a positive test result

def bayes_theorem(prior, sensitivity, specificity):
    evidence = (sensitivity * prior) + ((1 - specificity) * (1 - prior))
    posterior = (sensitivity * prior) / evidence
    return posterior

# 1% prevalence
prior = 0.01 

# True positive rate
sensitivity = 0.95

# True negative rate
specificity = 0.90

posterior = bayes_theorem(prior, sensitivity, specificity)
print("Probability pf disease given positive test: ", posterior)
