"""make a circular array"""

class CircularArray(object):

    def __init__(self):
        """instantiate CircularArray"""
        self.array = []
        self.head = None

    def add_item(self, item):
        """add an item to the array, just before head

        >>> circ = CircularArray()
        >>> circ.add_item("bonnie")
        >>> circ.head
        0

        """
        if self.head is None:
            # if not self.array:
            self.head = 0
            self.array = [item]
        else:
            # insert item
            self.array.insert(self.head, item)

            # reassign head
            self.head += 1

    def get_by_index(self, index):
        """return the data at a particular index

        >>> circ = CircularArray()
        >>> circ.add_item("aiden")
        >>> circ.add_item("kelly")
        >>> circ.add_item("leslye")
        >>> circ.get_by_index(1)
        'kelly'

        >>> circ = CircularArray()
        >>> circ.add_item("ashley")
        >>> circ.add_item("colleen")
        >>> circ.get_by_index(2)

        >>> circ = get_sample_array()
        >>> circ.rotate(1)
        >>> circ.get_by_index(4)
        'ashley'
        
        """

        # index doesn't exist the list
        if index >= len(self.array):
            return None

        # the easy case -- it doesn't go off the end of the list
        if index + self.head < len(self.array):
            return self.array[index + self.head]

        # the fun case: we have to go round the twist
        # shift left by length of array to get back into array index space
        adjusted_index = index + self.head - len(self.array)
        return self.array[adjusted_index]

    def rotate(self, increment):
        """rotate the array, positive for to the right, negative for to the left

        if increment is greater than the length of the list, keep going around

        -----> exercise left to the reader: fix doctests <-----

        >>> circ = get_sample_array()
        >>> circ.rotate(1)
        >>> circ.head
        0

        >>> circ = get_sample_array()
        >>> circ.rotate(1)
        >>> circ.rotate(-9)
        >>> circ.head
        2

        >>> circ = get_sample_array()
        >>> circ.rotate(3)
        >>> circ.rotate(12)
        >>> circ.head
        0

        >>> circ = get_sample_array()
        >>> circ.rotate(4)
        >>> circ.rotate(20)
        >>> circ.head
        4

        """

        # the aiden rule works for positive OR negative
        adjusted_index = (increment + self.head) % len(self.array)
        self.head = adjusted_index

def get_sample_array():
    circ = CircularArray()
    circ.add_item("ashley")
    circ.add_item("colleen") 
    circ.add_item("aiden") 
    circ.add_item("kelly")
    circ.add_item("leslye") 
    return circ


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
