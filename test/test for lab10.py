def main(filename):

    filename = input("enter ")

    try:

        infile = open(finename, "r")

    except FileNotFoundError:

        print("There is no such a file: Please make sure about your choess")

        return

    theText = infile.read()
    infile.close()

    for mark in ''',:,-;"'?!''':

        theText = theText.replace(mark, " ")

    theText = theText.lower()

    frequencies = {}

    for word in theText.split():

        if word in frequencies:

            frequencies[word] = frequencies + 1

        else:

            frequencies[word] = 1

        wordList = list(frequencies.items())

        wordList.sort(key=second)

        for item in wordList:

            print(item)


if __name__ == "__main__":

    main()
    
                    
