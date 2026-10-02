#  Plot and Explore Various Distributions

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm, binom, poisson, uniform

# Gaussian Distribution
x = np.linspace(-4, 4, 100)
plt.plot(x, norm.pdf(x, loc=0, scale=1), label= "Gaussian (u=0, s=1)")

#Binomial Distribution
n, p = 10.05
x = np.arange(0, n + 1)
plt.bar(x, binom.pmf(x, n, p), alpha=0.7, label = "Binomial(n=10, p=0.5)")

#Poisson Distribution
lam = 3
x = np.arange(0, 10)
plt.bar(x, poisson.pmf(x, lam), alpha=0.7, label="Poisson(l=3)")

#Uniform Distribution
x = np.random.uniform(low=0, high=10, size=1000)
sns.histplot(x, kde=True, label="Uniform", color="red")

plt.title("Probability Distribution")
plt.legend()
plt.show()