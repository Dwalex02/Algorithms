#
# Write here your implementation of Insertion Sort
#


def sort(data):

    for i in range(1, len(data)): #The array elements are traversed from 1 to n

        index = data[i]
        k = i - 1

        #Keep shifting until reaching index 0 or getting an element smaller than key
        while k >= 0 and index < data[k]:
            data[k + 1] = data[k]
            k = k - 1
        data[k + 1] = index

    return data #return the data so we can test it

