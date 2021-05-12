class Create:
    """Initializer of class takes series parameter and returns Class Objects"""
    def __init__(self, arr):
        """Built in validation and exception"""
        self._arr = arr
        self.ssort()


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

    def binarysearch(arr, l, r, x):

        while l <= r:

            mid = l + (r - l) // 2;

            # Check if x is present at mid
            if arr[mid] == x:
                print("Element is present at position % d" % mid)
                return mid

            # If x is greater, ignore left half
            elif arr[mid] < x:
                l = mid + 1

            # If x is smaller, ignore right half
            elif arr[mid] > x:
                r = mid - 1

            # If x is not present, it will say so


        print("Element is not present in array")
        return -1

# Getter
@property
def list(self):
    return self._arr


# Bubble Sort
y = [10, 33, 4, 17, 40]
if __name__ == "__main__":
    creates = Create(y.copy())
    print(y)
    print(creates._arr)

# Binary Search
x = 33
Create.binarysearch(creates._arr, 0, len(y)-1, x)

