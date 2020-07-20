# Linear and Binary Search assignment


def linear_search(arr, target):
    # Go through each value starting at the front
    # Check to see if it is equal to the target
        # Return index value if it is
    # Return -1 if not found in the array`

    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
    # If the target is in the array, return the index value
    # If the target is not in the array, return -1

def binary_search(arr, target):
    # Set first and last index values
    first = 0
    last = len(arr) -1

    # What is our looping criteria? What tells us to stop looping
    # If we see that the index position has gone past the end of the list we stop
    # If the value from the array is equal to the target, we stop 
    while first <= last:
        # Compare the target element to the midpoint of the array
            # Calculate the index of the midpoint
        mid = (first + last) //2        # The double slash rounds down

        # If the midpoint element matches our target, return the midpoint index
        if target == arr[mid]:
            return mid

        # If the midpoint value is not equal to the target, decide to go higher or lower
        if target < arr[mid]:
            # If target is less than the midpoint, toss all values greater than the midpoint
            # Do this by moving the search boundary high point down to one below the midpoint
            last = mid -1

        if target > arr[mid]:
            # If target is greater than the midpoint, toss all values less than the midpoint
            # Move the search boundary low point up to one above the midpoint
            first = mid + 1

        # Repeat this loop unitl the end of the array has been reached
        # When the mid index has surpassed the length of the list
    # If target is not found in the list, return -1
    return -1  
