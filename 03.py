organograma = {}
inputText = input()
organograma[inputText] = None

def getChildrems(father):
    leafs = []
    for child in father:
        if father[child]:
            leafs.append(father[child])
    return leafs

while inputText != "fim entrada":
    items = inputText.split(" ")
    for leaf in organograma:
        leafs = getChildrems(organograma)


# INCOMPLETO
    