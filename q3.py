def wordCount(t):
    """ Returns a dictionary with unique words encountered on which lines. """
    
    # We use dictionary because it can store the data in key value pair so a unique word will be the key and 
    # the number of occurences will be the value of it.
    wordsDict = {}

    # below syntax is used to open a file in read mode
    with open(t, 'r') as file:
        # enumrate function used to iterate over an iterable like here the file. It returns a tupple, line no. & line data.
        # Second argument start keeps count of the iterations here we need no. of lines so we will start it from 1.
        for lineNum, line in enumerate(file, start=1):
            # split will give us a list of words
            words = line.split()
            for word in words:
                if word in wordsDict:
                    # will add the line number in to the list as a value
                    wordsDict[word].append(lineNum)
                else:
                    # word is not present then we will add it with list of line number as a value.
                    wordsDict[word] = [lineNum]

    # (note: file will be automatically closed once the execution is completed.)
    return wordsDict;


if __name__ == "__main__":
    print(wordCount('test2.txt'))
