# Iterative and Bubble sorting assignment

# In-place selection sort
def selection_sort(arr):
    # loop through n elements
        # Minus one because we don't need to sort the very last item, 
        # it has already been sorted by the one before it
    for i in range(0, len(arr) -1):

        # Current index we are looking at, lowest index of the unsorted boundary
        boundary= i

        # Current value we are looking at, at the starting point of the unsorted boundary
        smallest_value = arr[boundary]

        # Current index of the lower end of the boundary
        smallest_index = boundary

        # Find the smallest element in the unsorted portion of the array
        # Unsorted array range is from the boundary line 
            # (which we are moving by 1 on each iteration of the first for loop)
        # to the end of the array
        for unsorted_index in range(boundary, len(arr)):
            # Iterate through the unsorted portion of the array and find the smallest value and its index location
            # Save that as the smallest value and smallest index
            if arr[unsorted_index] < smallest_value:
                smallest_value = arr[unsorted_index]
                smallest_index = unsorted_index
            
        # After iterating through all of the unsorted numbers and finding the smallest one,
        # Swap the found smallest value with the value at the begining of the boundary
        arr[boundary], arr[smallest_index] = arr[smallest_index], arr[boundary]

        # Then it will loop through on the next index of the whole array

    # When it has gone through the entire array, return the now sorted array
    return arr


def bubble_sort(arr):
    # Start at index 0 and iterate through each item in array
    # Compare element n to its next element.
    # If the next element is less than the first element, swap them and start back at index 0

    # Don't need to look at the last 
    for i in range(len(arr)-1):
        # Compare to the next item in the array
        # If the next value is less than the first value, swap them and start over
        if arr[i+1] < arr[i]:
            arr[i], arr[i +1] = arr[i+1], arr[i]
            bubble_sort(arr)

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
