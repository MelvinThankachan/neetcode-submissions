class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        if capacity > 0:
            self.array = []

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if len(self.array) >= self.capacity:
            self.resize()
        self.array.append(n)

    def popback(self) -> int:
        pop = self.array[-1]
        del self.array[-1]
        return pop

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return len(self.array)
    
    def getCapacity(self) -> int:
        return self.capacity
