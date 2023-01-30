#
# Write here your implementation of Insertion Sort
#


def is_balanced(string):
    stack = []

    #Traversing the string
    for i in string:
        if i in ["(", "{", "["]:

            #Insert the element in the stack
            stack.append(i)
        else:

            #An opening bracket must be always followed by a closing one
            if not stack:
                return False
            temp = stack.pop() #Pop fixed a problem where my anaconda test didn't pass, but pycharm tests did

            if temp == '(':
                if i != ")":
                    return False

            if temp == '{':
                if i != "}":
                    return False

            if temp == '[':
                if i != "]":
                    return False

    #Empty check
    if stack:
        return False
    return True