#Course: Data Structure , Author:Nazia Sharmin, assignment:Lab3B,instructor:Professor-Diego Aguirre,
# T.A.:Anindita Nath, date of last modification:None
class MyChainHashTable:

    def __init__(self, table):
        self.table = table
        self.slots = [ ]
        for i in range(self.table):
            self.slots.append([])

    def __str__(self):
        info = ""
        for items in self.slots:
            info += str(items)
        return info

    def insert(self, key):
        self.slots[self.hash_function(key)].append(key)
    def __len__(self):
        count = 0
        for i in self.slots:
            count += len(i)
        return count

    def hash_function(self, key):
        i = key % self.table
        return i


# convert base 26 letter to base 10 number
def base26LetterToBase10(string):
    string = string.lower()
    if string == " " or len(string) == 0:
        return 0
    if len(string) == 1:
        return ord(string)-96
    else:
        return base26LetterToBase10(string[1:])+(26**(len(string)-1))*(ord(string[0])-96)

# Convert base 10 int to base 26 letter
def base10ToBase26Letter(num):
    if num <= 0:
        return ""
    elif num <= 26:
        return chr(96+num)
    else:
        return base10ToBase26Letter(int((num-1)/26))+chr(97+(num-1)%26)

def readFile():
    with open("test.txt", encoding="utf-8") as file:
        x = [line.strip() for line in file]
    return x

def printBase10ToBase26(ht):
    for i in range(0, ht.table):
        print("[", end="")
        for j in range(0, len(ht.slots[i])):
            if j == (len(ht.slots[i]) - 1):
                print(base10ToBase26Letter(ht.slots[i][j]), end="")
            else:
                print(base10ToBase26Letter(ht.slots[i][j]), end=", ")
        print("]", end="")
    print("")

def get_load_factor(ht, wd):
    return wd / (ht.table)

def get_average_comparison(ht):
    total_lists, total_items = 0, 0
    for i in range(0, ht.table):
        if ht.slots[i]!=[]:
            total_lists += 1
        for j in range(0, len(ht.slots[i])):
            if len(ht.slots[i]) >= 1:
                total_items += 1
    #print("Total items", total_items, "Total lists", total_lists)
    print("Average comparison [average items per table's node]:",(total_items/total_lists))

# trying hash with size 2
x = MyChainHashTable(4)
y = MyChainHashTable(10)
z = MyChainHashTable(500)

words_in_file = readFile()

from nltk.corpus import words
#print("World" in words.words())

inserted_words = 0
for i in range(0, len(words_in_file)):
    if (words_in_file[i].lower() in words.words()):
        inserted_words += 1
        #print("English word, inserting...", words_in_file[i])
        x.insert(base26LetterToBase10(words_in_file[i]))
        y.insert(base26LetterToBase10(words_in_file[i]))
        z.insert(base26LetterToBase10(words_in_file[i]))
    #else:
        #print("Not an English word", words_in_file[i])

# printing hashtable as it is
print("Hashtable X [base10]:", x)
# print("table X:",x.table)
# print("Slots X:", len(x.slots))
# printing hashtable converted values
print("Hashtable X [base26]: ", end ="")
printBase10ToBase26(x)
print("Load factor for X:", str(get_load_factor(x, inserted_words)))
get_average_comparison(x)

print("Hashtable Y [base10]:", y)
print("Hashtable Y [base26]: ", end ="")
printBase10ToBase26(y)
print("Load factor for Y:", str(get_load_factor(y, inserted_words)))
get_average_comparison(y)

print("Hashtable Z [base10]:", z)
print("Hashtable Z [base26]: ", end ="")
printBase10ToBase26(z)
print("Load factor for Z:", str(get_load_factor(z, inserted_words)))
get_average_comparison(z)