
import argparse

# Quick Sort Implementation.
# Returns the index of the pivot element after partitioning
def partition(arr, low, high):
    pivot = arr[high]
    # print("pivot:", pivot)
    # Index of smaller element
    i = low - 1
    # print("initial i:", i)
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            # Swap elements at i and j to move smaller element to the left side
            arr[i], arr[j] = arr[j], arr[i]
    # Swap the pivot element with the element at i+1 because i is the index of the smaller element
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Recursive function to perform quick sort
def quick_sort(arr, low, high):
    # if low index is less than high index then only we need to sort
    if low < high:
        # pi is partitioning index, arr[pi] is now at right place
        pi = partition(arr, low, high)
        # print("pi :", pi)
        # Recursively sort elements before partition and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

if __name__ == "__main__":
    print("Quick Sort Implementation")
    parser = argparse.ArgumentParser(description="Quick Sort Algorithm")
    parser.add_argument("--elements", nargs="*", type=int, help="List of integers to sort")
    args = parser.parse_args()
    elements = args.elements
    print("Original array:", elements)
    quick_sort(elements, 0, len(elements) - 1)
    print("Sorted array:", elements)
