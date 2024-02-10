def checkIsPrime(n):
    """ Checks that a number is prime or not"""

    # The number must be greater than 2
    if n < 2:
        return False;
    # A number's factors will be 1, the number it self and no number more than the half of the number.
    # e.g. Factors of 12: 1,2,3,4,6,12 thats why we run the loop until the half+1 and typecast the number from float to int.    
    for i in range(2, int(n*0.5 + 1)):
        if n%i == 0:
            return False;    
    return True;      


def getPrimeNumbers(n):
    """ Returns a list of prime numbers from 2 to n. """
    
    pNumbers = [];
    # for range will only run until n doesn't include it thats why I used n+1 to include n as well. [2, n)
    for i in range(2, n+1):
        if checkIsPrime(i):
            # append is used to insert a new a element at the end of the list
            pNumbers.append(i);
    return pNumbers;        

# when this file will be imported somewhere then below code will not be executed!
# Here, __name__ will be __main__ but when we import it somewhere __name__ will be the file name like q1 here
if __name__ == "__main__":
    print(getPrimeNumbers(23))
