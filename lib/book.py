#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None  # Initialize with None or default value
        self.page_count = page_count  # This will call the setter method
    
    @property
    def page_count(self):
        """Getter method for page_count property"""
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_value):
        if isinstance(page_value, int):
            self._page_count = page_value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    

    
    
        