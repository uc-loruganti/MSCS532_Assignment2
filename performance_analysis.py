
import time
import tracemalloc
import random
import sys
from merge_sort import merge_sort
from quick_sort import quick_sort

# Set a higher recursion limit for Quick Sort
sys.setrecursionlimit(2000)

def run_sorting_algorithm(algorithm, data):
    tracemalloc.start()
    start_time = time.perf_counter()

    if algorithm.__name__ == "quick_sort":
        # Create a copy to sort in-place
        data_copy = data[:]
        algorithm(data_copy, 0, len(data_copy) - 1)
    else:
        # Merge sort returns a new sorted list
        sorted_data = algorithm(data[:])

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return (end_time - start_time) * 1000, peak / 1024

def generate_datasets(size):
    random_data = [random.randint(0, size) for _ in range(size)]
    sorted_data = sorted(random_data)
    reverse_sorted_data = sorted(random_data, reverse=True)
    return {
        "Random": random_data,
        "Sorted": sorted_data,
        "Reverse Sorted": reverse_sorted_data
    }

if __name__ == "__main__":
    dataset_sizes = [100, 500, 1000, 10000]
    algorithms = {
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }

    print("| Dataset Size | Data Type        | Algorithm    | Execution Time (ms) | Peak Memory (KB) |")
    print("|--------------|------------------|--------------|---------------------|------------------|")

    for size in dataset_sizes:
        datasets = generate_datasets(size)
        for data_type, data in datasets.items():
            for algo_name, algo_func in algorithms.items():
                time_taken, memory_used = run_sorting_algorithm(algo_func, data)
                print(f"| {size:<12} | {data_type:<16} | {algo_name:<12} | {time_taken:<19.4f} | {memory_used:<16.2f} |")
