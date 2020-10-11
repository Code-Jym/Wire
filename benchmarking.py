"""
This is where I test the speed of all the functions 
explicitly defined using time.perf_counter
"""

from wire import Wire
from time import perf_counter

def benchmark(func):
    """
    Benchmarks a function with it's function arguments 
    returns the time taken
    """

    def wrapper(func):
        # "starts" the timer (not really, just gets the current time)
        counter = []
        counter.append(perf_counter())

        func()

        counter.append(perf_counter())
        return counter[1] - counter[0] # returns the time taken
    
    return wrapper(func)


print("Time Taken For:")
alphabet = abcdefghijklmnopqrstuvwxyz

# Testing the Speed of Wire __init__ method
initCalls = benchmark(lambda: Wire(alphabet))
print(f"    -Wire.__init__: {initCalls}")

# Testing the Speed of Wire.getDiff method
string = Wire(alphabet)
print(benchmark(lambda: Wire(alphabet).getDiff(alphabet.upper())))
