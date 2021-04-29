class BubbleSort:
    """Initializer of class takes series parameter and returns Class Objects"""
    def __init__(self, arr):
        """Built in validation and exception"""
        self._arr = arr
        self.ssort()


    """Algorithm for building book series list, this id called from __init__"""
    def ssort(self):
        n = len(self._arr)
        # Traverse through all array elements
        for i in range(n):
            swapped = False

            # Last i elements are already
            #  in place
            for j in range(0, n-i-1):

                # traverse the array from 0 to
                # n-i-1. Swap if the element
                # found is greater than the
                # next element
                if self._arr[j] > self._arr[j+1] :
                    self._arr[j], self._arr[j+1] = self._arr[j+1], self._arr[j]
                    swapped = True

            # IF no two elements were swapped
            # by inner loop, then break
            if swapped == False:
                break

        """Getters with decorator to allow . notation access"""
    @property
    def list(self):
        return self._arr


if __name__ == "__main__":
    '''Value for testing'''

    '''Constructor of Class object'''
    x = [7, 8, 4, 32, 1, 3]
    bubbles = BubbleSort(x.copy())
    print(x)
    print(bubbles.list)