#
# The Move to Back program reads sequence of input characters one by one and maintain a linked list without duplicates.
# When you read in a previously unseen character, set it at the back of the list.
# When you read in a character that is already in the list, delete it from the list and reinsert it at the back of the list.
#
#

class Node:
    # We make a new class in order to use those varibles more easily
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    Implement here the linked list.

    NOTE: You might need to define additional operations in this class
    """
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        n = Node(data)

        #Empty check
        if self.head is None:
            self.head = n

        elif self.head.data >= n.data:
            n.next = self.head
            self.head = n

        else:
            #Locate the node before the insertion point
            temp = self.head
            while temp.next and n.data > temp.next.data:
                temp = temp.next

            #Insert
            n.next = temp.next
            temp.next = n

    def insert_at_back(self, data):
        newNode = Node(data)

        #empty check
        if self.head == None:
            self.head = newNode
            return
        else:
            #traverse to the last node
            temp = self.head
            while temp.next != None:
                temp = temp.next

            temp.next = newNode

    def delete(self, node):

        #checks if the node we are looking for is in the head
        if self.head.data == node:
            self.head = self.head.next
            return

        temp = self.head

        #locates the first occurrence of the key in the list
        while temp:

            if temp.data == node:
                break

            previous = temp
            temp = temp.next
            previous.next = temp.next

    def print(self):
        """
        Return the values as a comma-separated list (without spaces) stored in a string
        """
        if self.head == None:
            return ''
        else:
            curr = self.head
            list = []
            while curr != None: # appending the empty list with data
                list.append(str(curr.data)) #making the data type string
                curr = curr.next
            return ','.join(list)


class MoveToBack:
    """
    Implement here the Move To Back functionality.


    NOTE: You might need to define additional operations in this class
    """

    def __init__(self):
        self._internal_linked_list = LinkedList()

    def insert(self, c):
        #if the key is in the list delete it and put it at the end
        if c in self._internal_linked_list.print():
            self._internal_linked_list.delete(c)
            self._internal_linked_list.insert_at_back(c)
        #else insert it at the beginning
        else:
            self._internal_linked_list.insert(c)


    def get_sequence(self):
        return self._internal_linked_list.print()
