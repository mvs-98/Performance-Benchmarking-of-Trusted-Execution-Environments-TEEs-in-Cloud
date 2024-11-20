# Importing required libraries
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
import os

# Identify directory location of the current path
directory = os.path.dirname(os.path.abspath(__file__))

# Use standard order for machines and colors
csv_file_order = ['Without_SEV-SNP.csv', 'With_SEV-SNP.csv', 'Without_TDX.csv', 'With_TDX.csv']
machinecolors = ['blue', 'orange', 'green', 'red']
csv_file_names = ['Without_SEV-SNP', 'With_SEV-SNP', 'Without_TDX', 'With_TDX']

# Read data from CSV files
data_frames = []

for i, filename in enumerate(csv_file_order):
    fileloc = os.path.join(directory, filename)
    df = pd.read_csv(fileloc)
    # To use consistent name for machines
    df['Machine'] = csv_file_names[i] 
    # Assigning color to machines   
    df['Color'] = machinecolors[i] 
    # Converting training time to milliseconds
    df['Training Time'] *= 1000 
    # Converting standard deviation to milliseconds
    df['Training Time Std'] *= 1000  
    data_frames.append(df)

# Combine all data frames into one
all_data = pd.concat(data_frames)

models = all_data['Model'].unique()

num_models = len(models)
num_machines = len(csv_file_names)

width = 0.2
pos = [i for i in range(num_models)]

# Calculate maximum training time
max_training_time = all_data['Training Time'].max()

# Plotting the graph
plot.figure(figsize=(4, 5))

for i, machine in enumerate(csv_file_names):
    machine_data = all_data[all_data['Machine'] == machine]
    training_time_values = []
    training_time_std_values = []
    for model in models:
        model_data = machine_data[machine_data['Model'] == model]
        if not model_data.empty:
            training_time_values.append(model_data['Training Time'].values[0])
            training_time_std_values.append(model_data['Training Time Std'].values[0]/8)
        else:
            training_time_values.append(0)
            training_time_std_values.append(0)
    plot.bar([p + i * width for p in pos], training_time_values, width=width, color=machinecolors[i], label=machine, yerr=training_time_std_values, capsize=5)


plot.ylim(0, max_training_time + 1.0)

plot.xlabel('ML Models')
plot.ylabel('Training Time (milliseconds)')
plot.xticks([r + width * (num_machines / 2 - 0.5) for r in pos], models)
plot.yticks(np.arange(0, max_training_time + 1.0, 0.5))
plot.legend(title='Machines')
plot.tight_layout()
plot.savefig('Trainingtime.png')

