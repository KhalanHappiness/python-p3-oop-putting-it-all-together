#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand, size, condition ="New"):
        self.brand = brand
        self.size = size
        self.condition = condition

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size_value):
        if isinstance(size_value, int):
            self._size = size_value
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")

        




    