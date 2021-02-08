 # Inverted Index:
# Inverted Index is help to find the Number of Characters in Document means Apperance in docmuent.
# create a class of Inverted Index:
class InvertedIndex:
    # initlize the Constructor.
    def __init__(self, filename):
        # takes an parameter which is bascially open a text file in our directory
        self.file = open(filename)

# create a function Lower
    def Low(self):
        # pass the Variable and read the file
        content = self.file.read()
        # pass the vairable and spit the words into a list
        Lst = content.split(",")
        # after read and split close the file
        self.file.close()
        # pass the variable and create an array in which all words are in lower case
        x = [i.lower() for i in Lst]
        # the return function is bascially returns all the word in form of lower case
        return x


# create a function Word Count and takes a parameter
    def wordcount(self, var):
        # pass a variable in form of set.
        s = set(var)
        # return it and count it by using loop.
        return sorted([(i, var.count(i)) for i in s])


# create a function clean that takes an parameter
    def clean(self, x):
        # pass a variable with Empty String
        y = ' '
        # pass a variable and stores all the preposition in form of array
        s = ['.', ',', '-']
        # applying Loop
        for i in x:
            # check the condition
            if i in s:
                # if satisfied return continue the process
                continue
        # else increment
            else:
                y += i
        # than return
        return y


# create the function inverted index that takes a parameter text file
    def invertedindex(self, filename):
        # pass an empty Dictionary
        dictionary = {}
    # set as count 0
        lns = 0
    # applying loop and opening the file
        for line in open(filename):
            # increment the each line in respected document
            lns += 1
    # removing punctuations from the all lines.
            line = self.clean(line)
    # pass a variable and split all the lines
            l = line.split()
    # applying loop for each word in lines
            for word in l:
    # removing the stopwords
                if len(word) >= 2:
                # check condition
                    if word not in dictionary:
                    # first create empty dictionary
                        dictionary[word] = []
                    # append through line one
                        dictionary[word].append(1)
                    # append and return in form of list
                        dictionary[word].append([lns])
                    else:
                    # else applied with index zero and increment it
                        dictionary[word][0] += 1
                    # and at last it would be save in ln variable
                        dictionary[word][1].append(lns)

        print('List of dictionary : ')
        list_dictionary = list(dictionary)
    # sort the list d
        list_dictionary.sort()
    # applying loop
        for k in list_dictionary:
            # print and called the function wordcount for the count
            print(k, dictionary[k][0], self.wordcount(dictionary[k][1]))


# call the class
obj = InvertedIndex("project.txt")
obj.invertedindex("project.txt")
