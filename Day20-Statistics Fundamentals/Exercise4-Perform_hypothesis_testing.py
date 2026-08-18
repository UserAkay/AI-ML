# Q. Perform hypothesis testing on real-world datasets(e.g; comparing exam scores of two groups)

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

# Simulate exam scores for two groups
group_a = np.random.normal(loc=72, scale=8, size=100)   # e.g. traditional teaching
group_b = np.random.normal(loc=76, scale=8, size=100)   # e.g. new teaching method

# Hypotheses:
# H0: mean(group_a) == mean(group_b)
# H1: mean(group_a) != mean(group_b)

t_stat, p_value = stats.ttest_ind(group_a, group_b)

alpha = 0.05
print("---- Hypothesis Test: Independent t-test ----")
print(f"Group A mean: {group_a.mean():.2f}, std: {group_a.std():.2f}")
print(f"Group B mean: {group_b.mean():.2f}, std: {group_b.std():.2f}")
print(f"t-statistic: {t_stat:.3f}")
print(f"p-value:     {p_value:.4f}")

if p_value < alpha:
    print("Result: Reject H0 -> significant difference between groups")
else:
    print("Result: Fail to reject H0 -> no significant difference")

# Visualize
plt.hist(group_a, bins=20, alpha=0.6, label="Group A", color="steelblue", edgecolor="black")
plt.hist(group_b, bins=20, alpha=0.6, label="Group B", color="orange", edgecolor="black")
plt.axvline(group_a.mean(), color="steelblue", linestyle="--", linewidth=2)
plt.axvline(group_b.mean(), color="orange", linestyle="--", linewidth=2)

plt.title(f"Exam Scores: Group A vs Group B (p={p_value:.4f})")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.legend()
plt.show()