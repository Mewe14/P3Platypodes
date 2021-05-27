class Create:
    """Initializer of class takes series parameter and returns Class Objects"""
    def __init__(self, arr, find):
        """Built in validation and exception"""
        self._arr = arr
        self.ssort()
        self._find = find
        self._index = self.binarysearch()



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
                if self._arr[j] > self._arr[j+1]:
                    self._arr[j], self._arr[j+1] = self._arr[j+1], self._arr[j]
                    swapped = True

            # IF no two elements were swapped
            # by inner loop, then break
            if swapped == False:
                break

    def binarysearch(self):
        l = 0
        r = len(self._arr)-1

        while l <= r:

            mid = l + (r - l) // 2;

            # Check if desired value is present at mid
            if self._arr[mid] == self._find:
                return mid

            # If desired value is greater, ignore left half
            elif self._arr[mid] < self._find:
                l = mid + 1

            # If desired value is smaller, ignore right half
            elif self._arr[mid] > self._find:
                r = mid - 1

            # If desired value is not present, it will return -1
        return -1

    # Getters
    @property
    def list(self):
        return self._arr

    # this getter is used specifically for the binary search
    @property
    def index(self):
        return self._index


# Printing and testing code
if __name__ == "__main__":
    y = [10, 33, 4, 17, 40]
    find = 33
    # creates an object with the sorted list and desired value's position
    obj = Create(y.copy(), find)
    print(y)
    # the list is used to display the bubble sort
    print(obj.list)
    # the index is used to display the binary search
    print(obj.index)

