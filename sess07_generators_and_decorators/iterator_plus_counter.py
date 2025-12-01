# Python script to demonstrate a custom iterator

class PlusCounter:
    """
    A simple iterator that counts up from a starting number to an end number,
    incrementing it by a specified number (defaults to 1).

    Atrributes:
        current (int): The current value in the iteration.
        end (int): The end/maximum value(inclusive) the counter should reach.
        step (int): The value by which to increment the counter on each iteration.
    """
    def __init__(self,start,end,step=1):
        """
        Initialises the PlusCounter object/instance.

        Args:
            start (int): The starting value of the counter.
            end (int): The end/maximum value(inclusive) the counter should reach.
            step (int): The value by which to increment the counter on each iteration. Defaults to 1.
        """
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        """
        Returns the iterator object itself.

        Returns:
            PlusCounter: The iterator object/instance.
        """
        return self

    def __next__(self):
        """
        Returns the next value in the iterator. (or next number in the sequence)

        Raises:
            StopIteration: If the current value is greater than the end value.

        Returns:
            int: The next value in the iterator/sequence.
        """
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += self.step
            return self.current - 1

# Create/instantiate a PlusCounter object
my_counter1 = PlusCounter(1,10)

# Iterate over the counter object
for num in my_counter1:
    print(num)

print("\n")

# Create/instantiate another PlusCounter object to give the multiples of 5 from 1 - 75
my_counter2 = PlusCounter(1,75,5)

# Iterate over the counter2 object
for num in my_counter2:
    print(num)