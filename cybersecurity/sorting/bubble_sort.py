def bubble_sort(arr):
    n = len(arr)
    print(f"Original List: {arr}\n")

    # Traverse through all elements
    for i in range(n):
        print(f"Pass {i + 1}:")
        swapped = False  # To track if any swapping happens

        # Last i elements are already sorted, so ignore them
        for j in range(0, n - i - 1):
            print(f"  Comparing {arr[j]} and {arr[j + 1]}")

            # Swap if elements are in the wrong order
            if arr[j] > arr[j + 1]:
                print(f"  Swapping {arr[j]} and {arr[j + 1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            else:
                print("  No swap needed")

        print(f"Result after pass {i + 1}: {arr}\n")

        # If no elements were swapped, the list is sorted
        if not swapped:
            print("No swaps in this pass, so the list is sorted early!")
            break

    print(f"Final Sorted List: {arr}")
    return arr


# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)
