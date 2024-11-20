#!/bin/bash

# Declare and define an array to store operations
streamoperations=("Copy" "Scale" "Add" "Triad")

# Running the Stream benchmark for 5 times and collecting results
for i in {1..5}; do
    ./stream >> stream_output.txt
done

# Calculate average and standard deviation
> machinenameoutputfile.txt
for operation in "${streamoperations[@]}"; do
    grep "$operation:" stream_output.txt | awk '{print $2}' > "${operation}_values.txt"
    
    # Calculating the average
    avg=$(awk '{s+=$1} END {print s/NR}' "${operation}_values.txt")
    
    # Calculating the standard deviation
    std=$(awk '{sum+=$1; sumsq+=$1*$1} END {print sqrt(sumsq/NR - (sum/NR)**2)}' "${operation}_values.txt")
    
    # Put the results in output file
    echo "$operation: avg=$avg std=$std" >> machinenameoutputfile.txt
done
