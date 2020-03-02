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
Przysunąć przedmiot do <subst>endoskop||u|owi||em|ie</subst>.
Położyć przy <subst>endoskop||u|owi||em|ie</subst> lub przed <subst>endoskop||u|owi||em|ie</subst> lub
nad <subst>endoskop||u|owi||em|ie</subst> lub też pod <subst>endoskop||u|owi||em|ie</subst>.
Bez <subst>endoskop||u|owi||em|ie</subst>. Przerwa.
Trzymać daleko od <subst>endoskop||u|owi||em|ie</subst>.

<subst>książ|ka|ki|ce|kę|ką|ce</subst> leżała na stole. Włożyłam zakładkę do <subst>książ|ka|ki|ce|kę|ką|ce</subst>.

"""
Regex = re.compile(r'<subst>\S+</subst>') # dopisać, że może być kropka lub przecinek, ale nie musi?
Regex2 = re.compile(r'<adj>\S+</adj>')
list_of_subst = Regex.findall(text)
list_of_adj = Regex2.findall(text)
print(Regex.findall(text))

list_of_words = text.split(" ")
print(list_of_words)
#test
print(getIndexPositions(list_of_words, "<subst>endoskop||u|owi||em|ie</subst>"))

"""

for keyword in list_of_subst:
    #indexes = index for index, value in enumerate(list_of_words) if value = keyword
    counter_list = list(enumerate(my_list, 1)) if
        indexes = []
        idexes.append(index)
        for index in indexes:
            if list_of_words[index - 1] == "do":
                list_of_words[index] = Decline(keyword, "gen")

            """

#TODO assertion : assert element.split("|").len() = 6
"""
import numpy as np
values = np.array([1,2,3,1,2,4,5,6,3,2,1])
searchval = 3
ii = np.where(values == searchval)[0]

albo:
indices = [i for i, x in enumerate(my_list) if x == "whatever"]


# CONJUGATE THE KEYWORDS IN THE TEXT
for element in list:
    split_elelment = element.split("<subst>")
    prinom = split_elelment[0]
    element = split_elelment[1].replace("</subst>, "")
    if element.lower().startswith(" do ") or \
            element.lower().startswith(" od ") or \
            element.lower().startswith(" bez "):
        text=text.replace(element, element+gen(element))
    elif element.lower().startswith(" na ") or element.lower().startswith(" przy "):
        text = text.replace(element, element + miejscownik)
    elif element.lower().startswith(" nad ") or element.lower().startswith(" pod ") or element.lower().startswith(" przed "):
        text = text.replace(element, element + narzędnik)
#text.replace("przy "+word, "przy "+word+miejscownik )
print(text)
    """
