import argparse

# Merge Sort Implementation.
def merge_sort(arr):
    
    # arrays with 0 or 1 element are considered sorted
    if len(arr) <= 1:
        return arr

    # Find the middle index
    mid = len(arr) // 2
    
    # Split the array into two halves
    # Recursively split and merge. 
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the two sorted halves
    return merge(left_half, right_half)


# Helper function to merge two sorted arrays
def merge(left, right):
    sorted_array = []
    left_index = 0
    right_index = 0

    # Compare elements from both halves and merge them in sorted order
    # Iterate until we reach the end of either half
    while left_index < len(left) and right_index < len(right):
        # if left element is smaller, append it to the sorted array else append right element
        if left[left_index] < right[right_index]:  # For ascending order
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1

    # Append any remaining elements from both halves
    sorted_array.extend(left[left_index:])
    sorted_array.extend(right[right_index:])

    return sorted_array

if __name__ == "__main__":
    print("Merge Sort Implementation")
    parser = argparse.ArgumentParser(description="Merge Sort Algorithm")
    parser.add_argument("--elements", nargs="*", type=int, help="List of integers to sort")
    args = parser.parse_args()
    elements = args.elements
    print("Original array:", elements)
    sorted_array = merge_sort(elements)
    print("Sorted array:", sorted_array)