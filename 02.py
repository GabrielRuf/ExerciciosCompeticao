inputText = input()
inputText = inputText.replace(" ","")


def reversetext(text):
    reversedList = list(text)
    reversedList.reverse()
    return ''.join(reversedList)

canBePalindromo = False
Inlength = True
if len(inputText) >= 1 and len(inputText) <= 50:
    pass
else:
    Inlength = False

if inputText == reversetext(inputText) and Inlength:
    canBePalindromo = True
else:
    i = 0
    while i in range(0,(len(inputText)-1)) and not canBePalindromo:
        copy = inputText
        char1 = copy[i]
        j = i
        while j in range(0,(len(inputText)-1)):
            char2 = copy[j+1]
            copyList = list(copy)
            copyList[i] = char2
            copyList[j+1] = char1
            copy = ''.join(copyList)
            if copy == reversetext(copy):
                canBePalindromo = True
                break
            else:
                copy = inputText
            j+=1
        
        i+=1

if canBePalindromo:
    print(1)
else:
    print(0)