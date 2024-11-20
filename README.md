# Performance Benchmarking of Trusted Execution Environments (TEEs) in Cloud  

## Overview  
This project evaluates the performance overhead of modern Trusted Execution Environments (TEEs), such as **Intel TDX** and **AMD SEV-SNP**, for microservice-based workloads deployed on **Azure Confidential Virtual Machines**. The study provides insights into the trade-offs between enhanced security and performance impacts, helping optimize workloads in confidential computing environments.

## Features  
- **Micro and Macro Benchmarking**: 
  - Benchmarked critical metrics like **throughput**, **response time**, **memory**, and **I/O performance**.  
  - Used tools like **Redis**, **STREAM**, and **FIO** for robust performance analysis.  
- **Application Deployment**: 
  - Deployed Redis-based and Machine Learning-based microservices to simulate real-world workloads.  
- **Trade-off Analysis**: 
  - Analyzed the balance between security and performance in TEEs for confidential workloads.  
- **Cloud Integration**: 
  - Leveraged **Azure Confidential Virtual Machines** for secure execution of applications.  

## Technologies Used  
- **Trusted Execution Environments (TEEs)**: Intel TDX, AMD SEV-SNP  
- **Cloud Platform**: Azure Confidential Virtual Machines  
- **Benchmarking Tools**: Redis, STREAM, FIO  
- **Programming Language**: Python  
- **Microservice Frameworks**: Redis-based and Machine Learning workloads  

## Project Structure  
- `benchmarks/`: Contains scripts and configurations for running micro and macro benchmarks.  
- `microservices/`: Includes Dockerized microservices for Redis and ML-based workloads.  
- `results/`: Benchmark results and performance analysis reports.  
- `README.md`: Project documentation.  

## Prerequisites  
- **Cloud Environment**: Azure account with access to Confidential Virtual Machines.  
- **Python Environment**: Python 3.6+ installed.  
- **Benchmark Tools**: Redis, STREAM, and FIO installed on the target machines.  

## How to Run  
1. **Set Up Environment**:  
   - Launch Azure Confidential VMs with TDX or SEV-SNP support.  
   - Install required tools (`Redis`, `STREAM`, `FIO`) and dependencies.  

2. **Deploy Microservices**:  
   - Use the `microservices/` folder to build and deploy Docker containers for workloads.  
   - Example:  
     ```bash
     docker build -t redis-benchmark ./microservices/redis
     docker run -p 6379:6379 redis-benchmark
     ```  

3. **Run Benchmarks**:  
   - Execute scripts in the `benchmarks/` folder to run tests for throughput, latency, and I/O performance.  
   - Example:  
     ```bash
     python benchmarks/run_stream_benchmark.py
     ```  

4. **Analyze Results**:  
   - Review performance results stored in the `results/` directory.  
   - Use provided visualization scripts to generate performance graphs.  

## Results  
The project provides detailed insights into:  
- The impact of TEEs on application performance.  
- Metrics comparison for **Intel TDX** vs **AMD SEV-SNP**.  
- Optimization strategies for running workloads in secure environments.  

## Future Enhancements  
- Expand benchmarking to additional TEEs and cloud providers.  
- Explore hybrid workloads with TEEs in multi-cloud environments.  
- Develop automation pipelines for benchmark execution.  
