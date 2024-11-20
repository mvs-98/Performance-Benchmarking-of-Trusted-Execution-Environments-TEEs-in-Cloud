# Importing required libraries
import re
import matplotlib.pyplot as plot
import numpy as np

# Function to read from benchmark output from a file
def parse_benchmark_file(fn):
    with open(fn, 'r') as file:
        content = file.read()

    set_throughput = re.search(r'SET.*?(\d+\.\d+) requests per second', content, re.DOTALL)
    get_throughput = re.search(r'GET.*?(\d+\.\d+) requests per second', content, re.DOTALL)

    set_throughput_value = float(set_throughput.group(1)) if set_throughput else None
    get_throughput_value = float(get_throughput.group(1)) if get_throughput else None

    return set_throughput_value, get_throughput_value

# List of files to parse
files = ['benchmark.txt', 'benchmarksev.txt',
         'nontdxbenchmark.txt', 'tdxbenchmark.txt']

# Labels for each machine
labels = ['Without_SEV-SNP', 'With_SEV-SNP',
          'Without_TDX', 'With_TDX']

# Colors for each machine
colors = ['blue', 'orange', 'green', 'red']

# Initialize lists to store throughputs
set_throughputs = []
get_throughputs = []

# Reading data from each benchmark file
for fn in files:
    set_throughput, get_throughput = parse_benchmark_file(fn)
    set_throughputs.append(set_throughput)
    get_throughputs.append(get_throughput)

seterrors = [0.1 * throughput for throughput in set_throughputs]
geterrors = [0.1 * throughput for throughput in get_throughputs]

max_set_throughput = max(set_throughputs)
max_get_throughput = max(get_throughputs)
max_set_err = max(seterrors)
max_get_err = max(geterrors)

# Determine maximum y-axis value for graph plotting
set_y_maximum = (max_set_throughput + max_set_err) // 10000 * 10000 + 10000
get_y_maximum = (max_get_throughput + max_get_err) // 10000 * 10000 + 10000

# Plotting SET throughputs
plot.figure(figsize=(4, 5))
plot.bar(labels, set_throughputs, yerr=seterrors, color=colors, capsize=5)
plot.xlabel('SET Request')
plot.ylabel('Requests per Second')
plot.xticks(rotation=45, ha='right')
plot.ylim(0, set_y_maximum+10000)
plot.yticks(np.arange(0, set_y_maximum + 10000, 10000))
plot.tight_layout()
plot.savefig('throughputset.png')


# Plotting GET throughputs
plot.figure(figsize=(4, 5))
plot.bar(labels, get_throughputs, yerr=geterrors, color=colors, capsize=5)
plot.xlabel('GET Request')
plot.ylabel('Requests per Second')
plot.xticks(rotation=45, ha='right')
plot.ylim(0, get_y_maximum+10000)
plot.yticks(np.arange(0, get_y_maximum + 10000, 10000))
plot.tight_layout()
plot.savefig('throughputget.png')

