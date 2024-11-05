capitalLetters = list("ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ")
lowercaseLetters = list("йцукенгшщзхъфывапролджэячсмитьбю")
print("Введите строку")
string = input(str()) + ' '
print(string)
stringArray = list(string)
for i in range(len(stringArray)):
    if stringArray[i] in capitalLetters:
        stringArray[i] = lowercaseLetters[capitalLetters.index(stringArray[i])]
    else: continue
for i in range(len(stringArray)):
    print(stringArray[i], end='')
print('')

newStringArray = []
lastSpace = 0
for i in range(len(string)):
    if string[i] == ' ':
        newStringArray.append(string[lastSpace:i])
        lastSpace = i
    else: continue

maxVowelsWord = ''
maxVowelsWords = []
Vowels = list('аоеуэыяию')
maxVowels = 0
countVowels = 0
for i in range(len(newStringArray)):
    for j in range(len(newStringArray[i])):
        for k in range(len(newStringArray[i][j])):
            for n in range(len(Vowels)):
                if n == k:
                    countVowels += 1
            maxVowels = max(maxVowels, countVowels)
    maxVowelsWords.append(maxVowels)
    countVowels = 0
print(newStringArray[maxVowelsWords.index(maxVowels)])