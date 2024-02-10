def statsDecorator(func):
    # *args means any number of positional argumnets in a tupple. like we can pass (1,23,12,5). It is iterable.
    def wrapper(*args):
        numbers, lineNum = func(*args)
        # f string are used to write a variable or any datatype directly in a string
        print(f"For line no. {lineNum}:")
        print(f"The numbers read: {numbers}")
        print(f"The count of the numbers read: {len(numbers)}")
        print(f"The average of the numbers: {round(sum(numbers)/len(numbers),2)}")
        print(f"The maximum of the numbers: {max(numbers)}\n\n")
    return wrapper

@statsDecorator
def stats(nums, lineNum):
    """This return will invoke the decorator"""

    return nums, lineNum

def printStats(t):
     """This works as the main function and for each line will call the decoratored function. """
    with open(t,'r') as file:
        for lineNum, line in enumerate(file, start=1):
            numbers = line.split();
            # for each element in numbers typecast it to float and create a list from those numbers and assign back to numbers.
            numbers = list(map(float, numbers))
            # As question says calls a decorated function for every line
            stats(numbers, lineNum)


if __name__ == "__main__":
    printStats('test3.txt');
