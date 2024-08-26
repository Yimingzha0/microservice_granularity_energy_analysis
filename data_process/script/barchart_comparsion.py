# This file is used for plotting the bar chart of the average energy consumption of the six different systsems * granularities
import matplotlib.pyplot as plt
import re

averages = []
with open('../processed_data/Energy_Total_Data.txt', 'r') as file:
    for line in file:
        match = re.search(r'Average = ([\d.]+)', line)
        if match:
            averages.append(float(match.group(1)))

group_averages = []
for i in range(0, len(averages), 6):
    group = averages[i:i+6]
    group_averages.append(sum(group) / len(group))

labels = ['Pet-Coarse', 'Pet-Medium', 'Pet-Fine', 'Train-Coarse', 'Train-Medium', 'Train-Fine']
plt.figure(figsize=(10, 6))
bars = plt.bar(labels, group_averages)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.2f}',
             ha='center', va='bottom')
plt.ylabel('Average Energy (Joules)')
plt.ylim(0, max(group_averages) * 1.1)
plt.tight_layout()
plt.show()