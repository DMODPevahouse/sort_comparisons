# ----- Script Creator
# ----- David Pevahouse
# ----- Date
# ----- 12/05/2022
# ----- Purpose ------
# This script is used to test the quick sorts of different variations to test efficiency
#
#
# ----- Description ------
# This script will take in an array of data that data_objects created and then perform the requested quick sort on the
# data


# this function takes in an array, picks the first item as a pivot and does a quick sort
def recursive_first_pivot_sort(array, e, c):
    if len(array) <= 1:
        return array, e, c
    pivot = array[0]
    left = []
    right = []
    for i in range(1, len(array)):
        if array[i] < pivot:
            left.append(array[i])
            e += 1
        else:
            right.append(array[i])
            e += 1
        c += 1
    left_sorted, e1, c1 = recursive_first_pivot_sort(left, e, c)
    right_sorted, e2, c2 = recursive_first_pivot_sort(right, e, c)
    left_sorted.append(pivot)
    finished_array = left_sorted + right_sorted
    final_e = e1 + e2
    final_c = c1 + c2
    return finished_array, final_e, final_c


# this function takes in an array and a value, and performs a quick sort until the partition is under the value then
# does an insertion sort
def recursive_quick_insertion_sort(array, k, e, c):
    if len(array) <= k:
        final_a, final_e, final_c = insertion_sort(array, e, c)
        return final_a, final_e, final_c
    pivot = array[0]
    left = []
    right = []
    for i in range(1, len(array)):
        if array[i] < pivot:
            left.append(array[i])
            e += 1
        else:
            right.append(array[i])
            e += 1
        c += 1
    left_sorted, e1, c1 = recursive_quick_insertion_sort(left, k, e, c)
    right_sorted, e2, c2 = recursive_quick_insertion_sort(right, k, e, c)
    left_sorted.append(pivot)
    finished_array = left_sorted + right_sorted
    final_e = e1 + e2
    final_c = c1 + c2
    return finished_array, final_e, final_c


def insertion_sort(array, e, c):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
            e += 1
        c += 1
    return array, e, c


# this function takes in an array, does a median of three, then performs a quick sort
def recursive_median_of_three_quick_sort(array, e, c):
    if len(array) <= 1:
        return array, e, c
    pivot = median_of_three(array, e, c)
    left = []
    right = []
    for i in range(0, len(array)):
        if array[i] < pivot:
            left.append(array[i])
            e += 1
        elif array[i] > pivot:
            right.append(array[i])
            e += 1
        c += 1
    left_sorted, e1, c1 = recursive_median_of_three_quick_sort(left, e, c)
    right_sorted, e2, c2 = recursive_median_of_three_quick_sort(right, e, c)
    left_sorted.append(pivot)
    finished_array = left_sorted + right_sorted
    final_e = e1 + e2
    final_c = c1 + c2
    return finished_array, final_e, final_c


def median_of_three(array, e, c):
    first = array[0]
    middle = array[len(array) // 2]
    last = array[len(array) - 1]
    if first < middle < last or last < middle < first:
        return middle
    elif middle < first < last or last < first < middle:
        return first
    else:
        return last