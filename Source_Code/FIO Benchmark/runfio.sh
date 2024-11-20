#!/bin/bash

# Declaring required variables for running fio benchmark
n="randread"
ie="libaio"
id=4
rwvalue="randread"
bsvalue="4k"
direct=1
size="1G"
numofjobs=1
runntime=60
group_reporting=1
filename="fio_result.txt"

# Running fio benchmark and displaying output on terminal
fio --name=$n --ioengine=$ie --iodepth=$id --rw=$rwvalue --bs=$bsvalue --direct=$direct --size=$size --numjobs=$numofjobs --runtime=$runntime --group_reporting | tee $filename 

# Displaying results of fio output on terminal
cat $filename
