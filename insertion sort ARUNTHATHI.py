def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage
arr = [12,34,32,36,35,3]
print("Original array:", arr)
insertion_sort(arr)
print("Sorted array:", arr)
