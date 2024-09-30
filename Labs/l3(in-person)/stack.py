class Stack:
    def __init__(self):
        """Initialize an empty stack using a list."""
        self.items = []

    def __len__(self):
        return len(self.items)

    def is_empty(self):
        """Check if the stack is empty
            Returns:
            bool: True if the stack is empty, False otherwise.
        """
        # TODO: Implement the is_empty method
        return len(self.items) == 0

    def push(self, item):
        """Push an item onto the top of the stack.
            Args:
            item: The item to be pushed onto the stack.
        """
        # TODO: Implement the push method
        self.items.append(item)

    def pop(self):
        """Remove and return the item from the top of the stack.

            Returns:
            The item at the top of the stack.

            Raises:
            IndexError: If the stack is empty.
        """
        # TODO: Implement the pop method with proper error handling
        if self.is_empty():
            raise IndexError("Pop operation on an empty stack...")
        return self.items.pop()

    def peek(self):
        """Return the item at the top of the stack without removing it.

            Returns:
            The item at the top of the stack.

            Raises:
            IndexError: If the stack is empty.
        """
        # TODO: Implement the peek method with proper error handling
        if self.is_empty():
            raise IndexError("Peek operation on an empty stack...")
        return self.items[-1]
    