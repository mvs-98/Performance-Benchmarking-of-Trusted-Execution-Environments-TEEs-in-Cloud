# Importing required libraries
import csv
import time
import numpy as np

# Loading Iris dataset
from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

# Importing machine learning models
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Function to train models and calculate average training time and standard deviation
def ml_benchmark(model_class, X_train, X_test, y_train, y_test, runs=5):
    model_accuracies = []
    model_training_times = []

    for _ in range(runs):
        model = model_class()
        starttime = time.time()
        model.fit(X_train, y_train)
        endtime = time.time()
        
        accuracy = model.score(X_test, y_test)
        training_time = endtime - starttime

        model_accuracies.append(accuracy)
        model_training_times.append(training_time)

    average_accuracy = np.mean(model_accuracies)
    average_training_time = np.mean(model_training_times)
    standard_training_time = np.std(model_training_times)

    return average_accuracy, average_training_time, standard_training_time

# Main function
def main():
    # Loading the dataset
    data = load_iris()
    X, y = data.data, data.target

    # Splitting the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Benchmarking the models
    dectreet_accuracy, dectreet_training_time, dectreet_training_time_std = ml_benchmark(DecisionTreeClassifier, X_train, X_test, y_train, y_test)
    svm_accuracy, svm_training_time, svm_training_time_std = ml_benchmark(SVC, X_train, X_test, y_train, y_test)
    nbiase_accuracy, nbiase_training_time, nbiase_training_time_std = ml_benchmark(GaussianNB, X_train, X_test, y_train, y_test)

    # Storing results to a csv file
    with open('Without_SEV-SNP.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Model', 'Accuracy', 'Training Time', 'Training Time Std'])
        writer.writerow(['Decision Tree', dectreet_accuracy, dectreet_training_time, dectreet_training_time_std])
        writer.writerow(['SVM', svm_accuracy, svm_training_time, svm_training_time_std])
        writer.writerow(['Naive Bayes', nbiase_accuracy, nbiase_training_time, nbiase_training_time_std])

    print("Benchmark results saved to 'Without_SEV-SNP.csv'.")

if __name__ == "__main__":
    main()
