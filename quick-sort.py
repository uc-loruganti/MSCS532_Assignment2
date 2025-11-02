import argparse

# Quick Sort Implementation.
def quick_sort(arr):
    print("Sorting array using Quick Sort...")

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) - 1]
    less_than_pivot = []
    greater_than_pivot = []
    equal_to_pivot = []

    print("pivot:", pivot)

    for element in arr:
        if element < pivot:
            less_than_pivot.append(element)
        elif element > pivot:
            greater_than_pivot.append(element)
        else:
            equal_to_pivot.append(element)
    # print("Less than pivot:", less_than_pivot)
    # print("Greater than pivot:", greater_than_pivot)
    # Recursively sort the less than and greater than pivot lists
    sorted_less = quick_sort(less_than_pivot) if less_than_pivot else []
    sorted_greater = quick_sort(greater_than_pivot) if greater_than_pivot else []

    return sorted_less + equal_to_pivot + sorted_greater

if __name__ == "__main__":
    print("Quick Sort Implementation")
    parser = argparse.ArgumentParser(description="Quick Sort Algorithm")
    parser.add_argument("--elements", nargs="*", type=int, help="List of integers to sort")
    args = parser.parse_args()
    elements = args.elements
    print("Original array:", elements)
    sorted_array = quick_sort(elements)
    print("Sorted array:", sorted_array)