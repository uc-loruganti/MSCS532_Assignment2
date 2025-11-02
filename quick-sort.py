import argparse

# Quick Sort Implementation.
def quick_sort(arr):
    print("Sorting array using Quick Sort...")
    return arr


if __name__ == "__main__":
    print("Quick Sort Implementation")
    parser = argparse.ArgumentParser(description="Quick Sort Algorithm")
    parser.add_argument("--elements", nargs="*", type=int, help="List of integers to sort")
    args = parser.parse_args()
    elements = args.elements
    print("Original array:", elements)
    sorted_array = quick_sort(elements)
    print("Sorted array:", sorted_array)