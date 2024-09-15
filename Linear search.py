def linear_search(arr, x):
    # Traverse through all elements in the list
    for i in range(len(arr)):
        # Check if the current element matches the target value
        if arr[i] == x:
            return i  # Return the index of the found element
    return -1  # Return -1 if the element is not found

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

    # Get the element to search for
    x = int(input("Enter the number to search for: "))

    # Perform linear search
    result = linear_search(arr, x)

    # Output the result
    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present in the array")

# Call the main function
if __name__ == "__main__":
    main()
