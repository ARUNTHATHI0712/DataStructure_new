def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # If x is present at the middle
        if arr[mid] < x:
            low = mid + 1
        # If x is present at the left half
        elif arr[mid] > x:
            high = mid - 1
        # x is present at mid
        else:
            return mid

    # x is not present in the array
    return -1

# Function to take user input and store it in a list
def get_user_input():
    # Prompt user to enter numbers separated by spaces
    user_input = input("Enter sorted numbers separated by spaces: ")
    # Convert the input string into a list of integers
    arr = list(map(int, user_input.split()))
    return arr

# Main function
def main():
    # Get the sorted array from user input
    arr = get_user_input()

    # Get the element to search for
    x = int(input("Enter the number to search for: "))

    # Perform binary search
    result = binary_search(arr, x)

    # Output the result
    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present in the array")

# Call the main function
if __name__ == "__main__":
    main()
