from scipy.stats import ttest_ind

#Sample Datasets
group1 = [2.1, 2.5, 2.8, 3.0, 3.2]
group2 = [1.0, 2.0, 2.4, 2.7, 2.9]

#Perform t-test
t_stat, p_value = ttest_ind(group1, group2)
print("T-Statistic: ", t_stat)
print("P-value: ", p_value)

#Interpretation
alpha = 0.5
if p_value < alpha:
    print("Reject the null hypothesis : significant difference")
else:
    print("Fail to reject the null hypothesis : no significant difference")
