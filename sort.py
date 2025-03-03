def pivot_sort(arr):
    """
    Sorts an array using the pivot sort (similar to quicksort) algorithm.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: A new list with the elements from arr sorted in ascending order.
    """
    if len(arr) <= 1:
        # Base case: an array of zero or one elements is already sorted
        return arr
    pivot = arr[0]

    # Partition the array into two sub-arrays:
    # 'left' with elements less than the pivot
    # 'right' with elements greater than or equal to the pivot
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]

    # Recursively sort the sub-arrays and combine them with the pivot
    return pivot_sort(left) + [pivot] + pivot_sort(right)
