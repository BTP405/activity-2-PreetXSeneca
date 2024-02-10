import matplotlib.pyplot as plt

def graphSnowfall(t):
    """ Creates a bar graph from provided file data and using matplotlib. """
    
    ranges = ["0-10", "11-20", "21-30", "31-40", "41-50"]
    # Creats a list to store the count of occurrences for each range
    counts = [0] * len(ranges)

    with open(t, 'r') as file:
        for line in file:
            cms = int(line)
            # now to count the number of occurances
            
            for index, r in enumerate(ranges):
                # getting each element from ranges with index then spliting them from '-' and converting into 
                # int and then checking that read number is between them or not if it is then at that index
                # we increase the count.
                lowerLimit, upperLimit = map(int, r.split('-'))
                
                if lowerLimit <= cms <= upperLimit:
                    # if it is in that range will increase the count for that index
                    # ALo, we will not move forward and break the loop
                    counts[index] += 1
                    break

     # fig is the figure object, and ax is a single axis or an array of subplot axis.
    fig, ax = plt.subplots()
    # takes x-axis and y-axis
    ax.bar(ranges, counts)
    ax.set_ylabel("Number of occurrences")
    ax.set_xlabel("Ranges (cms)")
    ax.set_title("Snowfall accumulation")

    plt.show()

if __name__ == "__main__":
    graphSnowfall('test.txt')
