class Jar:
    def __init__(self, capacity=12):
        if capacity<0:
            raise ValueError
        self._size=0
        self._capacity=capacity

    def __str__(self):
        return self.size*"🍪"

    def deposit(self, n):
        if n>self.capacity:
            raise ValueError("exceeded capacity")
        if self.size+n>self.capacity:
            raise ValueError("exceeded capacity")
        self._size+=n

    def withdraw(self, n):

        if self.size<n:
            raise ValueError("no more left")
        self._size-=n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jar = Jar()

jar.deposit(5)
jar.withdraw(4)

print(jar)
