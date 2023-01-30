# ----- Script Creator
# ----- David Pevahouse
# ----- Date
# ----- 12/05/2022
# ----- Purpose ------
# Algorithms to take in a linked list and sort it
#
#
# ----- Description ------
# This file has all of the functions to take in a linked list and perform a natural merge sort on it
#


# this function takes in a linked list and performs a natural merge sort
def natural_merge_sort(node, e, c):
    if node is None:
        return node, e, c
    if node.next is None:
        return node, e, c
    left = node
    right = split_list(node)
    left, e, c = natural_merge_sort(left, e, c)
    right, e, c = natural_merge_sort(right, e, c)
    return merge(left, right, e, c)


# this function takes in a linked list and splits it in half
def split_list(node):
    if node is None:
        return node
    if node.next is None:
        return node
    slow = node
    fast = node.next
    while fast is not None:
        fast = fast.next
        if fast is not None:
            slow = slow.next
            fast = fast.next
    temp = slow.next
    slow.next = None
    return temp


def merge(left, right, e, c):
    if left is None:
        return right, e, c
    if right is None:
        return left, e, c
    if left.data < right.data:
        result = left
        result.next, e, c = merge(left.next, right, e+1, c+1)
    else:
        result = right
        e += 1
        result.next, e, c = merge(left, right.next, e+1, c+1)
    c += 1
    return result, e, c
