import numpy as np

def generate_data():
    data = np.random.random(1000)
    mean = np.mean(data)
    std = np.std(data)
    return data, mean, std

def analyze_distribution(data, mean, std):
    result = {}
    result["within_1_std"] = np.sum((data >= mean - std) & (data <= mean + std))
    result["within_2_std"] = np.sum((data >= mean - 2*std) & (data <= mean + 2*std))
    result["within_3_std"] = np.sum((data >= mean - 3*std) & (data <= mean + 3*std))
    return result

data, mean, std = generate_data()
distribution = analyze_distribution(data, mean, std)

print("Mean:", mean)
print("Standard Deviation:", std)
print("Distribution analysis:", distribution)
