import random


teacherss = ["Mr.Mortenson", "Mrs.Mansour", "Mr.Eckman", "Mr.Simmons", "Mrs.Decaprio"]


class teacher:
    """Initializer of class takes series parameter and returns Class Objectg"""
    def __init__(self, series):
        """Built in validation and exception"""
        if series < 0 or series > 7:
            raise ValueError("Series must be between 2 and 10")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.teacherss()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

    """Algorithm for building Fibonacci sequence, this id called from __init__"""
    def teacherss(self):
        limit = self._series
        f = [(random.sample((teacherss), k=2))]  # fibonacci starting array/list
        while limit > 0:
            self.set_data(f[0])
            f = [f[0]]
            limit -= 1

    """Method/Function to set Fibonacci data: list, dict, and dictID are instance variables of Class"""
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
    '''Value for testing'''
    a = 2
'''Constructor of Class object'''
teach = teacher(a/a)
print(f"Here are some math recommendations = {teach.list}")

#for i in range(a):
#print(f"Listing of Book Recs {i}= {bookrecs.get_sequence(i)}")

