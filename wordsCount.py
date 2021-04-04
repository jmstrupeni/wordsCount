#wordsCount v1
import argparse
from re import sub
from json import dumps

parser = argparse.ArgumentParser(
    description = 'Script to count the frequency of each word in a text file, producing an output in JSON format.')
parser.add_argument('textFile', help='text file to analyze')
args = parser.parse_args()

try:
    oFile = open(args.textFile)
except FileNotFoundError:
    raise SystemExit(f'File not found {args.textFile}')

output = {}
header = {}
wordsCount = {}
totalWordsCount = 0
wordsInLine = str

for line in oFile:
    wordsInLine = line.split(' ')
    for i in wordsInLine:
        i = sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ]','',i.lower())
        if len(i)>0:
            totalWordsCount += 1
            if i in wordsCount:
                wordsCount[i] += 1
            else:
                wordsCount[i] = 1
oFile.close()

header['textFile'] = args.textFile
header['totalWordsCount'] = totalWordsCount
output['header'] = header
# Reverse order.
wordsCount = dict(sorted(wordsCount.items(), key=lambda item: item[1], reverse=True))
output['wordsCount'] = wordsCount
jsonString = dumps(output, ensure_ascii=False)
print(jsonString)
