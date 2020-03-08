#! python3
import re

glossary = ["<subst>endoskop||u|owi||em|ie</subst>", "<subst>teleskop||u|owi||em|ie</subst>", "<subst>książ|ka|ki|ce|kę|ką|ce</subst>" ]
# Function decline nouns
def Decline(keyword, case):
    ''' Decline nouns and adjectives '''
    if case == 'nom':
        endings = keyword.split("|")
        result = endings[0] + endings[1]
    elif case == 'gen':
        endings = keyword.split("|")
        result = endings[0] + endings[2]
    elif case == 'dat':
        endings = keyword.split("|")
        result = endings[0] + endings[3]
    elif case == 'acc':
        endings = keyword.split("|")
        result = endings[0] + endings[4]
    elif case == 'inst':
        endings = keyword.split("|")
        result = endings[0] + endings[5]
    elif case == 'loc':
        endings = keyword.split("|")
        result = endings[0] + endings[6]
    return result
#TEST FUNKCJI:
print(Decline(glossary[2], 'nom'))
print(Decline(glossary[2], 'gen'))
print(Decline(glossary[2], 'dat'))
print(Decline(glossary[2], 'acc'))
print(Decline(glossary[2], 'inst'))
print(Decline(glossary[2], 'loc'))

def getIndexPositions(listOfElements, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    indexPosList = []
    indexPos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            indexPos = listOfElements.index(element, indexPos)
            # Add the index position in list
            indexPosList.append(indexPos)
            indexPos += 1
        except ValueError as e:
            break

    return indexPosList

# FINDING KEYWORDS IN THE TEXT

text  ="""
Zamontować cewnik na <subst>endoskop||u|owi||em|ie</subst>. Przygotować <subst>endoskop||u|owi||em|ie</subst>.
Przysunąć przedmiot do <subst>teleskop||u|owi||em|ie</subst>.
Położyć przy <subst>endoskop||u|owi||em|ie</subst> lub przed <subst>endoskop||u|owi||em|ie</subst> lub
nad <subst>endoskop||u|owi||em|ie</subst> lub też pod <subst>endoskop||u|owi||em|ie</subst>.
Bez <subst>endoskop||u|owi||em|ie</subst>. Przerwa.
Trzymać daleko od <subst>endoskop||u|owi||em|ie</subst>.

<subst>książ|ka|ki|ce|kę|ką|ce</subst> leżała na stole. Włożyłam zakładkę do <subst>książ|ka|ki|ce|kę|ką|ce</subst>.

"""
Regex = re.compile(r'<subst>\S+</subst>') # dopisać, że może być kropka lub przecinek, ale nie musi?
Regex2 = re.compile(r'<adj>\S+</adj>')
list_of_subst = list(set(Regex.findall(text)))
list_of_adj = list(set(Regex2.findall(text)))
print(list_of_subst)
print(len(list_of_subst))

#add spaces before .,;: to separate the keywords
text = text.replace(".", " .").replace(",", " ,").replace(";", " ;").replace(":", " :").replace("\n", " \n ") # todo cudzysłów, \n itd
list_of_words = text.split(" ")

print(list_of_words)
# 1. NOUNS
# indexing all NOUNS
list_of_indexes =[]
for element in list_of_subst:
    indexes = getIndexPositions(list_of_words, element)
    for index in indexes:
        list_of_indexes.append(index)
list_of_indexes.sort()
print(list_of_indexes)

# Decline words inside list:

for index in list_of_indexes:
    print(index)
#genitif
    if list_of_words[index - 1].lower() == "bez" \
            or list_of_words[index - 1].lower() == "blisko" \
            or list_of_words[index - 1].lower() == "dla" \
            or list_of_words[index - 1].lower() == "do" \
            or list_of_words[index - 1].lower() == "dookoła" \
            or list_of_words[index - 1].lower() == "koło" \
            or list_of_words[index - 1].lower() == "koło" \
            :
        list_of_words[index] = Decline(list_of_words[index], "gen")

    else:
        list_of_words[index] = Decline(list_of_words[index], "nom")

print(list_of_words)

#print(getIndexPositions(list_of_words, "<subst>endoskop||u|owi||em|ie</subst>"))


#TODO assertion : assert element.split("|").len() = 6
