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
    else:
        # Choose the first element as the pivot
        pivot = arr[0]
        # Elements less than or equal to the pivot
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        # Elements greater than the pivot
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        # Recursively sort the sublists and concatenate them with the pivot
        return pivot_sort(less_than_pivot) + [pivot] + pivot_sort(greater_than_pivot)

# Example usage
#if __name__ == "__main__":
#    sample_list = [34, 7, 23, 32, 5, 62]
#    sorted_list = pivot_sort(sample_list)
#    print("Sorted list:", sorted_list)
