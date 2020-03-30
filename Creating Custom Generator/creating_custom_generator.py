class SquareNumbers:
    def __init__(self, n, hop=1):
        self.n = n
        self.hop = hop
        self.counter = 0

    def square(self, number):
        return number**2

    def __next__(self):
        sn = self.square(self.counter)
        self.counter += self.hop
        return sn 

squared_numbers = SquareNumbers(1000000000000, 28)
print(next(squared_numbers))
print(next(squared_numbers))
print(next(squared_numbers))
print(next(squared_numbers))
print(next(squared_numbers))
print(next(squared_numbers))
print(next(squared_numbers))