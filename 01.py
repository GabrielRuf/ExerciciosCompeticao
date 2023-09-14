rawText = input()

textWithoutSpaces = rawText.replace(" ","")

binaryText = ""
count = 0
currentPosition = 0
binaryList = []

for char in textWithoutSpaces:
    if char.islower():
        binaryText += "0"
    else:
        binaryText += "1"
    count += 1
    
    isinfinal = currentPosition == (len(textWithoutSpaces)-1)
    if count == 8 or isinfinal:
        count = 0
        binaryList.append(binaryText)
        binaryText = ""
    currentPosition += 1


TranslatedText = ""
print(binaryList)
for BinaryChar in binaryList:
    TranslatedText += chr(int(BinaryChar,2))

print(TranslatedText)