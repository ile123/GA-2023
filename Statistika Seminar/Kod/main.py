from helper_functions import read_exe_file
import pandas as pd
import numpy as np
from scipy.stats import t, norm
import matplotlib.pyplot as plt
import statistics
import math

def arithmetic_mean(data: list):
    return np.mean(data)


def modulo(data: list):
    return statistics.mode(data)


def median_of_an_sample(data: list):
    return np.median(data)


def characteristic_five_of_an_sample(data: list):
    return {
        "Median": median_of_an_sample(data),
        "1st Quartile": np.percentile(data, 25),
        "3rd Quartile": np.percentile(data, 75),
        "Minimum": min(data),
        "Maximum": max(data)
    }


def variance_of_the_data(data: list):
    return np.var(data)


def standard_deviation_of_data(data: list):
    return np.std(data)


def interquartile_range_of_data(data: list):
    return np.percentile(data, 75) - np.percentile(data, 25)


def range_of_data(data: list):
    return np.max(np.array(data)) - np.min(np.array(data))


def create_frequency_distribution(data, class_width=1000):
    bins = np.arange(np.min(data), np.max(data) + class_width, class_width)
    frequencies, bin_centers = np.histogram(data, bins=bins)
    return pd.DataFrame({
        'Interval': [(bin_centers[i], bin_centers[i+1]) for i in range(len(bin_centers)-1)],
        'Frequency': frequencies,
        'Class Width': class_width
    })


def create_relative_frequency_distribution(frequency_distribution):
    total = frequency_distribution['Frequency'].sum()
    return pd.DataFrame({
        'Interval': frequency_distribution['Interval'],
        'Relative Frequency': frequency_distribution['Frequency'] / total
    })


def create_cumulative_relative_frequency_distribution(relative_frequency_distribution):
    cumulative_relative_frequency = relative_frequency_distribution['Relative Frequency'].cumsum()
    return pd.DataFrame({'Interval': relative_frequency_distribution['Interval'],
                        'Cumulative Relative Frequency': cumulative_relative_frequency})


def calculate_confidence_interval(data: list, confidence_level=90):
    mean, std = np.mean(data), np.std(data, ddof=1)
    n, alpha = len(data) - 1, 1 - confidence_level
    margin_of_error = t.ppf(1 - alpha / 2, n) * (std / np.sqrt(n))
    lower_bound, upper_bound = mean - margin_of_error, mean + margin_of_error
    return (lower_bound, upper_bound)


def hypothesis_test(data, hypothesis_mean, significance_level):
    sample_size, sample_mean, std_dev = len(data), np.mean(data), np.std(data)

    z_score = (sample_mean - hypothesis_mean) / (std_dev / np.sqrt(sample_size))
    critical_value = norm.ppf(1 - (significance_level / 2))

    return z_score, critical_value


def main():
    data = read_exe_file("p16.xlsx")
    mean = arithmetic_mean(data)
    mod = modulo(data)
    median = median_of_an_sample(data)
    variance = variance_of_the_data(data)
    standard_deviation = standard_deviation_of_data(data)
    interquartile_range = interquartile_range_of_data(data)
    range_of_sample = range_of_data(data)
    number_of_classes = math.ceil(math.sqrt(len(data)))
    class_width = (np.max(data) - np.min(data)) / number_of_classes
    frequenciey = create_frequency_distribution(data, class_width)
    relative_frequencie = create_relative_frequency_distribution(frequenciey)
    cumulative_relative_frequencie = create_cumulative_relative_frequency_distribution(relative_frequencie)
    confidence_90 = calculate_confidence_interval(data, 0.9)
    confidence_95 = calculate_confidence_interval(data, 0.95)
    confidence_99 = calculate_confidence_interval(data, 0.99)
    z_score, critical_value = hypothesis_test(data, 2642, 0.05)


    print(f"""
Data: {data}\n
Size of data: {len(data)}\n 
Mean: {mean}\n
Modulo: {mod}\n
Median: {median}\n
Characteristic five of an sampel: {characteristic_five_of_an_sample(data)}\n
Variance: {variance}\n
Standard deviation: {standard_deviation}\n
Interquartile Range: {interquartile_range}\n
Range: {range_of_sample}\n\n
""")
    print(f"\n{frequenciey}\n\n{relative_frequencie}\n\n{cumulative_relative_frequencie}\n")
    print(f"\n\nConfidence level 90%: {confidence_90}\n\nConfidence level 95%: {confidence_95}\n\nConfidence level 99%: {confidence_99}\n\n")
    print("Z Score: ", z_score)
    print("Critical Value: ", critical_value)

    if np.abs(z_score) > critical_value:
        print("Failed to reject the null hypothesis")
    else:
        print("Reject the null hypothesis")

    plt.figure(figsize=(12, 6))
    plt.subplot(2, 2, 1)
    plt.hist(data, bins=number_of_classes, edgecolor='black')
    plt.title('Frequency Histogram')
    plt.xlabel('Average Student Cost')
    plt.ylabel('Frequency')

    plt.subplot(2, 2, 2)
    plt.hist(data, bins=number_of_classes, weights=np.zeros_like(data) + 1. / len(data), edgecolor='black')
    plt.title('Relative Frequency Histogram')
    plt.xlabel('Average Student Cost')
    plt.ylabel('Relative Frequency')

    frequencies, bin_edges = np.histogram(data, bins=number_of_classes)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

    plt.subplot(2, 1, 2)
    plt.plot(bin_centers, frequencies, marker='o', linestyle='-')
    plt.title('Frequency Polygon')
    plt.xlabel('Average Student Cost')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()