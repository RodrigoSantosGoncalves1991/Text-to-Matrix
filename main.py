
def ConvertTxtToArray(path):
    f = open(path, 'r', encoding='utf-8')
    text = f.read()
    arrayText = text.replace("\n", " ").split(" ")
    return arrayText

def handleString(arrayText, filter):
    arrayData = []
    for word in arrayText:
        if word:
            filter_word = ''.join(w for w in word if w not in filter).lower()
            arrayData.append(filter_word)
    return arrayData

def analyzingWordOccurrences(filteredTextArray):
    wordDict = {}
    while len(filteredTextArray) > 0:
        word = filteredTextArray[0]
        j = 0
        count = 0
        while j < len(filteredTextArray):
            if word == filteredTextArray[j]:
                filteredTextArray.pop(j)
                count += 1
            j += 1
        wordDict[word] = count
    return wordDict

def generateProbabilityHistogram(wordDict):
    top20 = {}
    count = 0
    for i in sorted(wordDict, key=wordDict.get, reverse=True):
        top20[i] = wordDict[i]
        count += 1
        if count >= 20:
            break
    import matplotlib.pyplot as plt
    names = list(top20.keys())
    import numpy as np
    values = (np.array(list(top20.values())) / np.sum(list(wordDict.values()))) * 100
    plt.title("Probabilidade de ocorrência de palavras do texto(Top 20)")
    plt.text(9.0, 4.0, "Total de palavras do texto: {}".format(np.sum(list(wordDict.values()))))
    plt.xlabel("Palavras do texto em Latim")
    plt.ylabel("Probabilidade (%)")
    plt.xticks(rotation=45, ha='right')
    plt.bar(names, values)
    plt.show()

def ConvertArrayToTxt(arrayText, nameFile):
    textRead = ""
    for word in arrayText:
      if word:
        textRead = textRead + " " + word
      else:
        textRead = textRead + "\n\n" + word
    file = open(f'texto lido - {nameFile}', 'w')
    file.write(textRead)

if __name__ == '__main__':
    print("Base Text - Matrix Representation I")
    arrayText = ConvertTxtToArray('Base Text - Matrix Representation I - v2.txt')
    filteredTextArray = handleString(arrayText, ".,;()")
    wordDict = analyzingWordOccurrences(filteredTextArray)
    generateProbabilityHistogram(wordDict)
    ConvertArrayToTxt(arrayText,'Base Text - Matrix Representation I - v2.txt')


    print("Base Text - Matrix Representation II")
    arrayText = ConvertTxtToArray('Base Text - Matrix Representation II - v2.txt')
    filteredTextArray = handleString(arrayText, '.,;()?:""')
    wordDict = analyzingWordOccurrences(filteredTextArray)
    generateProbabilityHistogram(wordDict)
    ConvertArrayToTxt(arrayText,'Base Text - Matrix Representation II - v2.txt')