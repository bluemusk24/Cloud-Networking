# Quick Sort in Python
# Idea: Divide and Conquer
# 1. Choose a pivot
# 2. Partition: put smaller elements on the left, larger on the right
# 3. Recursively sort the sublists

def quick_sort(arr, depth=0):
    indent = " " * depth  # for pretty printing recursion depth

    # Base case: if the array has 0 or 1 elements, it's already sorted
    if len(arr) <= 1:
        print(f"{indent}Returning {arr} (already sorted)")
        return arr

    # Choose pivot (here: middle element)
    pivot = arr[len(arr) // 2]
    print(f"{indent}Pivot chosen: {pivot} from {arr}")

    # Partition step
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    print(f"{indent}Left: {left}, Middle: {middle}, Right: {right}")

    # Recursively apply quicksort to left and right, combine results
    return quick_sort(left, depth + 1) + middle + quick_sort(right, depth + 1)


# Example usage
numbers = [10, 7, 8, 9, 1, 5]
print("Original List:", numbers, "\n")
sorted_numbers = quick_sort(numbers)
print("\nFinal Sorted List:", sorted_numbers)
