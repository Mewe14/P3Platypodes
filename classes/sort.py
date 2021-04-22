import random


math_classes = ["Calculus AB", "Integrated 1", "Integrated 2", "Integrated 3", "Calculus BC", "AP Stats", "Compacted Math", "Trigonometry"]


class mathematics:
    """Initializer of class takes series parameter and returns Class Object"""
    def __init__(self, maths):
        """Built in validation and exception"""
        if maths < 0 or maths > 7:
            raise ValueError("Series must be between 2 and 10")
        self._maths = maths
        self._list = []
        self._dict = {}
        self._dictID = 0
        self.math_class()

    """Algorithm for building random sequence, this id called from __init__"""
    def math_class(self):
        f = [(random.sample((math_classes), k=self._maths))]  # random starting array/list
        self.set_data(f[0])
        f = [f[0]]

    """Method/Function to set random data: list, dict, and dictID are instance variables of Class"""
    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1


    """Getters with decorator to allow . notation access"""
    @property
    def series(self):
        return self._series

    @property
    def list(self):
        return self._list

    @property
    def number(self):
        return self._list[self._dictID - 1]

    """Traditional Getter requires method access"""
    def get_sequence(self, nth):
        return self._dict[nth]



if __name__ == "__main__":
    '''Constructor of Class object'''
    math = mathematics(2)
    print(f"Here are some math recommendations = {math.list}")


