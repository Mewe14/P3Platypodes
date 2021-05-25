

class sophiebubble:

    def __init__(self):
        self._lst=[]

    def sorty_original(sorty_test):
        sorty_var1 =  sorty_test
        return sorty_var1.split(',')


    def bubbleSort(value_1):

        n = len(value_1)-3
        value_sorty = value_1
        arr = value_sorty.split(',')
        value = arr

        # Traverse through all array elements
        for i in range(n):
            # Last i elements are already in place
            for j in range(0, n-i-1):
                if value[j] > value[j+1]:
                    value[j], value[j+1] = value[j+1], value[j]
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            # Driver code to test above


            return value


