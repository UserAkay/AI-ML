import numpy as np

#Generate random dataset
dataset = np.random.randint(1, 51, size = (5,5) )
print("Originaal: \n", dataset)

#Filter vector > 25 and replace with 0
dataset[dataset > 25] = 0
print("Modified Dataset: \n", dataset)

#Calculate Summary state
print("Sum: ", np.sum(dataset))
print("Mean: ", np.mean(dataset))
print("Standard Deviation: ", np.std(dataset))
