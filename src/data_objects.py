# ----- Script Creator
# ----- David Pevahouse
# ----- Date
# ----- 12/05/2022
# ----- Purpose ------
# Create data structures to be sorted
#
#
# ----- Description ------
# This file has all the functions that are used to create the linked list and array from a file that is being passed
# to it from main and then it passes those created data structures back to main in order for it to use them to be sorted
from data_checks import is_operand_number


# this class creates a node for the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def add_node(self, data):
        if self.next is None:
            self.next = Node(data)
        else:
            self.next.add_node(data)

    def print_list(self):
        print(self.data)
        if self.next is not None:
            self.next.print_list()


# this function takes in a file and creates an array of the data
def create_array(file):
    data = open(file, "r")
    array = []
    for line in data:
        i = 0
        for char in line:
            if is_operand_number(char):
                j = i
                j += 1
                while j < len(line) - 1 and is_operand_number(line[j]):
                    char = char + line[j]
                    j += 1
                if i > 0 and is_operand_number(line[i - 1]):
                    pass
                else:
                    array.append(int(char))
            i += 1
    return array


# this function creates a linked list from a file
def create_linked_list(file):
    data = open(file, "r")
    head = None
    for line in data:
        i = 0
        for char in line:
            if is_operand_number(char):
                j = i
                j += 1
                while j < len(line) - 1 and is_operand_number(line[j]):
                    char = char + line[j]
                    j += 1
                if i > 0 and is_operand_number(line[i-1]):
                    pass
                elif head is None:
                    head = Node(int(char))
                else:
                    head.add_node(int(char))
            i += 1
    return head
