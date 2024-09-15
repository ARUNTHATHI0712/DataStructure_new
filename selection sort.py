def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Function to take user input and store it in a list
def get_user_input():
    # Prompt the user to enter numbers separated by spaces
    user_input = input("Enter numbers separated by spaces: ")
    # Convert the input string into a list of integers
    arr = list(map(int, user_input.split()))
    return arr

# Main function
def main():
    # Get the array from user input
    arr = get_user_input()

    # Sort the array using Selection Sort
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)

# Call the main function
if __name__ == "__main__":
    main()
