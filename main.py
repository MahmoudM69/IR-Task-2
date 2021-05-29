import re


def read_format(doc):
    document = open(doc, encoding="utf8")
    D = document.read()
    document.close()
    D = D.lower()
    D = re.sub(r'[^\w\s]', '', D)
    D = D.strip()
    D = D.split(" ")
    return D


docindx = 1


def fs_list_creator(d):
    global docindx
    dlist = [None] * len(d)
    for i in range(len(d)):
        dlist[i] = [d[i], docindx]
    docindx += 1
    return dlist


D1 = read_format("Doc1.txt")
Doc1 = fs_list_creator(D1)


D2 = read_format("Doc2.txt")
Doc2 = fs_list_creator(D2)


D3 = read_format("Doc3.txt")
Doc3 = fs_list_creator(D3)

nowords = D1 + D2 + D3
nowords.sort()


words = Doc1 + Doc2 + Doc3
words = sorted(words, key=lambda words: str(words[0]))

word = [None, None]
for i in range(len(words)):
    try:
        word = words[i]
        count = words.count(word)
        for r in range(count-1, 0, -1):
            del words[r+i]
        words[i].append(count)
    except IndexError as error:
        break
preword = words

word = [None, None, None]
temp = [None, None, 0, []]
for x in range(len(words)):
    NDoc = 1
    try:
        word = words[x]
        temp[0] = word[0]
        temp[1] = NDoc
        temp[2] += word[2]
        temp[3].append([word[1], word[2]])
        while x < len(words)-1:
            if word[0] == words[x+1][0]:
                NDoc += 1
                temp[1] = NDoc
                temp[2] += words[x+1][2]
                temp[3].append([words[x+1][1], words[x+1][2]])
                del words[x+1]
            else:
                break
    except IndexError as error:
        break
    words[x] = temp
    word = [None, None, None]
    temp = [None, None, 0, []]


for k in range(len(words)):
    string = "{0} {1:9} | {2} {3:3} | {4} {5:3}  |   Posting: Doc,Freq".format(
        "Term:", words[k][0], "N Docs:", words[k][1], "Coll Freq:", words[k][2])
    print(string)
    for l in range(len(words[k][3])):
        print("                                                              {}".format(
            words[k][3][l]))
    print(" ")
