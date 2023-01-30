class Node:
    #We make a new class in order to use those varibles more easily
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert_at_beginning(self, data):
        n=Node(data)
        n.next=self.head

        if self.head != None: #empty list check
            self.head.prev=n #old head's previous pointer will now refer to newly created node
            self.head=n #new node becomes the new head
            n.prev=None

        else:
            #make new node both head and tail
            self.head=n
            self.tail=n
            n.prev=None #both pointers refer to None


    def insert_at_position(self, data, position):
        n=Node(data)
        size=int(self.size())
        if position<=size:

            if position == 0:
                self.insert_at_beginning(data)
            else:
                for i in range(1,position):
                    self.head=self.head.next #to point the position
                #changing the pointers
                n.prev=self.head
                n.next=self.head.next
                self.head.next.prev=n #assign it in order to insert between them
                self.head.next=n

        else:
            raise ValueError

    def insert_at_end(self, data):
        n=Node(data)
        n.prev = self.tail

        if self.tail == None:
            self.head = n
            self.tail = n
            n.next = None # the first element's previous pointer has to refer to None

        else: # If list is not empty, change pointers accordingly
            self.tail.next = n
            n.next = None
            self.tail = n

    def delete_at_beginning(self):
        #We simply set the start node to None
        self.head=self.head.prev
        self.head=None

    def delete_at_position(self, position):
        size=int(self.size())
        if position <= size: #Checking for the ValueError

            if position == 0: #We already have a function for this
                self.delete_at_beginning()
            else:
                temp = self.head
                #Get the pointer to the node at position n by traversing the doubly linked
                #list up to the nth node from the beginning. Then we delete the node
                while temp != None:
                    next = temp.next

                    if temp.data == position:
                        if temp.prev:
                            temp.prev.next = temp.next
                        else:
                            self.head = temp.next
                        if temp.next:
                            temp.next.prev = temp.prev
                        else:
                            self.tail = temp.prev
                    temp = next

        else:
            raise ValueError

    def delete_at_end(self):
        #nce we reach the last node, we set the next reference of the node previous to the last node,
        #to None which actually removes the last node.
        if self.head != self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

        else:
            self.head = self.tail = None



    def print_forward(self):
        """
        Must return a String
        """
        curr = self.head

        if self.head == None:
            return None

        list=[]

        while curr != None: # appending the empty list with data
            list.append(str(curr.data)) #making the data type string
            curr = curr.next

        return ','.join(list) #geting rid of the brackets of the list and the space separator

    def print_backward(self):
        """
        Must return a String
        """
        #same idea like the previous function
        curr = self.head

        if self.head == None:
            return None

        list = []

        while curr != None:
            list.append(str(curr.data))
            curr = curr.next

        list.reverse() #backwards
        return ','.join(list)

    def size(self):
        size=0
        temp=self.head

        while temp != None: #counting the nodes in the list
            size += 1
            temp=temp.next

        return size


    def get_first(self):
        """
        Return the value of the first node or None if there's no nodes
        """
        if self.head == None:
            return None
        else:
            return self.head.data

    def get_last(self):
        """
        Return the value of the last node or None if there's no nodes
        """
        if self.tail == None:
            return None
        else:
            return self.tail.data

    def get_previous_node(self, node):
        #same idea as the print_forward
        size = int(self.size())

        if node <= size:
            curr = self.head

            if self.head == None:
                return None

            list = []

            while curr != None:
                list.append(str(curr.data))
                curr = curr.next

            p=list[node-2] #-2 means the previous node
            return int(p)

        else:
            raise ValueError

    def get_next_node(self, node):
        # same idea as the print_forward
        curr = self.head
        size = int(self.size())

        if node <= size:

            if self.head == None:
                return None

            list = []

            while curr != None:
                list.append(str(curr.data))
                curr = curr.next

            p = list[node]#[node] already means the next node by indexing

            return int(p)

        else:
            raise ValueError

    def contains(self, value):

        x = 1
        cond = False
        temp = self.head

        if self.head == None: #Checks whether the list is empty
            return False

        while temp != None:

            if temp.data == value: #traversing the list looking for if there is match between the data and the value
                cond = True
                break

            temp = temp.next
            x += 1 #increasing the value not to enter infinite loop

        if cond:
            return True
        else:
            return False

