# ----- Script Creator
# ----- David Pevahouse
# ----- Date
# ----- 12/05/2022
# ----- Purpose ------
# These are general functions that are used in the program to the data to determine
# its type, such as operators, operands, and numbers. It will also check if the
# data is valid, such as if there are too many operands or operators
# ----- Description ------
# There are several simple functions in this category that will be called as needed
# to determine what the data is and allow for if statements to be used whenever we
# need to check for a specific type of data or make sure that a specific type of data
# is needed. It takes in a value, makes a comparison and returns true or false

# This function checks if it is an operator
def is_operator(text):
    if text == "+" or text == "-" or text == "*" or text == "/" or text == "$" or text == "%" or text == "<" or text == ">":
        return True
    else:
        return False


# This function checks if it is an operand
def is_operand(text):
    if ("0" <= text <= "9") or ("a" <= text <= "z") or ("A" <= text <= "Z") or text == "<" or text == ">":
        return True
    else:
        return False


# This function checks if it is a number
def is_operand_number(text):
    if "0" <= text <= "9":
        return True
    else:
        return False


# This function checks if the data is a leter
def is_operand_letter(text):
    if "a" <= str(text) <= "z" or "A" <= str(text) <= "Z":
        return True
    else:
        return False


# This function checks to make sure that there is at least one operand in the line
def any_operands(text):
    operand_exists = False
    i = len(text)
    i -= 1
    while i >= 0:
        if is_operand(text[i]):
            operand_exists = True
        i -= 1
    return operand_exists


# This function checks to make sure there is at least one operator in the line
def any_operators(text):
    operator_exists = False
    i = len(text)
    i -= 1
    while i >= 0:
        if is_operator(text[i]):
            operator_exists = True
        i -= 1
    return operator_exists

