
# Insertion Sort in Python
# Idea: Build the sorted list one element at a time.
# For each element, insert it into the correct position
# among the elements before it.


def insertion_sort(arr):
    print(f"Original List: {arr}\n")
    # Start from the 2nd element (index 1), since the first element is "sorted"
    for i in range(1, len(arr)):
        key = arr[i] # Current element to insert
        j = i - 1
        print(f"Step {i}: Insert {key} into the sorted part {arr[:i]}")
        # Shift elements of the sorted portion that are greater than key
        while j >= 0 and arr[j] > key:
            print(f" {arr[j]} is greater than {key}, shifting {arr[j]} to the right")
            arr[j + 1] = arr[j]
            j -= 1
            # Place key at its correct position
            arr[j + 1] = key
            print(f"Inserted {key}, current list: {arr}\n")
            print(f"Final Sorted List: {arr}")
    return arr
    

# Example usage
numbers = [12, 11, 13, 5, 6]
insertion_sort(numbers)