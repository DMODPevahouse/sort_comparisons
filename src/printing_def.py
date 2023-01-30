# ----- Script Creator
# ----- David Pevahouse
# ----- Date
# ----- 12/05/2022
# ----- Purpose ------
# Print data to a file
#
#
# ----- Description ------
# These functions take in a linked list or an array and print it to a file
#


# this function takes in a linked list then prints it to a file
def print_linked_list(node, file):
    file.write(str(node.data) + " ")
    if node.next is not None:
        print_linked_list(node.next, file)


# this function takes in an array and prints it to a file
def print_array(array, file):
    for i in range(len(array)):
        file.write(str(array[i]) + " ")