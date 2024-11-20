# Importing required libraries
import os
import numpy as np
import re
import matplotlib.pyplot as plot

# Function for reading benchmark outputs from a file
def read_benchmark_data(file_location):
    with open(file_location, 'r') as file:
        readlines = file.readlines()
    
    get_request_time = None
    set_request_time = None
    

    for input in range(len(readlines)):  
        
        if 'GET' in readlines[input]:
            patternmatch = re.search(r'(\d+) requests completed in ([0-9.]+) seconds', readlines[input+1])
            if patternmatch:
                get_request_time = float(patternmatch.group(2))
        
        if 'SET' in readlines[input]:
            patternmatch = re.search(r'(\d+) requests completed in ([0-9.]+) seconds', readlines[input+1])
            if patternmatch:
                set_request_time = float(patternmatch.group(2))

    return set_request_time, get_request_time


# Function for gathering benchmarking data
def gather_benchmark_data(machine_type, numofreq):
    set_request_data = []
    get_request_data = []
    for request in numofreq:
        file_location = f'{machine_type}_{request}.txt'
        if os.path.exists(file_location):
            set_request_time, get_request_time = read_benchmark_data(file_location)
            set_request_data.append(set_request_time if set_request_time is not None else 0)
            get_request_data.append(get_request_time if get_request_time is not None else 0)
        else:
            set_request_data.append(0)
            get_request_data.append(0)
    return set_request_data, get_request_data


# Function to calculate standard deviation
def calculate_standard_deviation(data):
    return np.std(data)

# List containing request numbers to test
numofreq = [1000, 2000, 4000, 8000, 10000]

# Gathering data for all four machines
machines_type = ['noofreq', 'noofreqsev', 'nontdxnoofreq', 'tdxnoofreq']
machinelabels = ['Without_SEV-SNP', 'With_SEV-SNP', 'Without_TDX', 'With_TDX']
gathered_set_data = []
gathered_get_data = []
gathered_set_std_dev = []
gathered_get_std_dev = []

for machinetype in machines_type:
    set_data, get_data = gather_data(machinetype, numofreq)
    gathered_set_data.append(set_data)
    gathered_get_data.append(get_data)
    gathered_set_std_dev.append([calculate_standard_deviation(set_data) / 8] * len(numofreq))
    gathered_get_std_dev.append([calculate_standard_deviation(get_data) / 8] * len(numofreq))

# Logic to determine maximum y-axis limit and tick marks
max_set_request_value = max([max(data) for data in gathered_set_data] + [max(std) for std in gathered_set_std_dev])
max_get_request_value = max([max(data) for data in gathered_get_data] + [max(std) for std in gathered_get_std_dev])
max_y_axis = max(max_set_request_value, max_get_request_value)
maximum_y_ticks = (max_y_axis // 0.05 + 1) * 0.05

# Plot the graph for SET requests
width = 0.2
indexvalue = np.arange(len(numofreq))
plot.figure(figsize=(4, 5))
for itrate, label in enumerate(machinelabels):
    plot.bar(indexvalue - width*1.5 + itrate*width, gathered_set_data[itrate], width, yerr=gathered_set_std_dev[itrate], label=f'{label}', capsize=5)
plot.xlabel('Number of SET Requests')
plot.ylabel('Response Time (seconds)')
plot.xticks(indexvalue, numofreq)
plot.ylim(0, max_y_axis + 0.05)
plot.yticks(np.arange(0, max_y_axis + 0.05, 0.05))
plot.legend()
plot.tight_layout()
plot.savefig('set_requests_graph.png')


# Plot the graph for GET requests
plot.figure(figsize=(4, 5))
for itrate, label in enumerate(machinelabels):
    plot.bar(indexvalue - width*1.5 + itrate*width, gathered_get_data[itrate], width, yerr=gathered_get_std_dev[itrate], label=f'{label}', capsize=5)
plot.xlabel('Number of GET Requests')
plot.ylabel('Response Time (seconds)')
plot.xticks(indexvalue, numofreq)
plot.ylim(0, max_y_axis + 0.05)
plot.yticks(np.arange(0, max_y_axis + 0.05, 0.05))
plot.legend()
plot.tight_layout()
plot.savefig('get_requests_graph.png')

