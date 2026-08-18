# Calculate Confidence intervals for properties in a datasets

import numpy as np
from scipy import stats

data = np.random.normal(loc=500, scale=80, size=200)

mean = np.mean(data)
sem = stats.sem(data)

ci_low, ci_high = stats.t.interval(0.95, df=len(data)-1, loc=mean, scale=sem)

print(f"Mean: {mean:.2f}")
print(f"95% Confidence Interval: ({ci_low:.2f}, {ci_high:.2f})")