inf = open('text1.txt','r', encoding= 'utf')
words = []

for line in inf.readlines():
    words.extend(line.lower().strip().split())

wordsDict = dict()
for word in words:
    word = word.strip('., /?{}[]()!@#$%^&*')
    # if word not in wordsDict:
    #     wordsDict[word] = 1
    # else:
    #     wordsDict[word] = wordsDict[word]+1
    wordsDict[word]=wordsDict.get(word,0) + 1

# for key, val in wordsDict.items():
#     print(f'{key} - {val}')

words = [(key,val) for key, val in wordsDict.items()]
words = sorted(sorted(words, key = lambda x: x[0]), key = lambda  x: x[1], reverse=True)
for m in words:
    print(*m)

