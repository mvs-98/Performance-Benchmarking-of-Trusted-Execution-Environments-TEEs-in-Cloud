# Importing required libraries
import matplotlib.pyplot as plot
import numpy as np

# Function to read from output text files
def read_file(file_path):
    average_values = []
    std_dev_values = []
    with open(file_path, 'r') as file:
        for line in file:
            sections = line.split()
            average_values.append(float(sections[1].split('=')[1]))
            std_dev_values.append(float(sections[2].split('=')[1]))
    return average_values, std_dev_values

labels = ['Copy', 'Scale', 'Add', 'Triad']

without_sev_avg, without_sev_std_dev = read_file('Without_SEV-SNP.txt')
with_sev_avg, with_sev_std_dev = read_file('With_SEV-SNP.txt')
without_tdx_avg, without_tdx_std_dev = read_file('Without_TDX.txt')
with_tdx_avg, with_tdx_std_dev = read_file('With_TDX.txt')

# Locations of the lables
x = np.arange(len(labels))  
# Setting the bar width
width = 0.2  

# Plotting the graph based on extracted values
fig, ax = plot.subplots(figsize=(4, 5))
rects1 = ax.bar(x - width*1.5, without_sev_avg, width, yerr=without_sev_std_dev, label='Without_SEV-SNP', color='blue', capsize=5)
rects2 = ax.bar(x - width/2, with_sev_avg, width, yerr=with_sev_std_dev, label='With_SEV-SNP', color='orange', capsize=5)
rects3 = ax.bar(x + width/2, without_tdx_avg, width, yerr=without_tdx_std_dev, label='Without_TDX', color='green', capsize=5)
rects4 = ax.bar(x + width*1.5, with_tdx_avg, width, yerr=with_tdx_std_dev, label='With_TDX', color='red', capsize=5)

# Adding text in graph for labels, custom x-axis tick labels, and so on.
ax.set_xlabel('Stream Operations')
ax.set_ylabel('Bandwidth (MB/s)')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(title='Machines')
ax.set_ylim(10000, ax.get_ylim()[1])

fig.tight_layout()
# Save the graph
plot.savefig('StreamPlot.png')
