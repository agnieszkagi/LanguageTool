#! python3
import re
import morfeusz2

# def()


def Decline_Noun(keyword, case):
    ''' Decline nouns and adjectives '''
    result = ""
    morf = morfeusz2.Morfeusz()
    list_of_morphosyntactic_forms = morf.generate(keyword)
    if case == 'nom':
        for tuple in list_of_morphosyntactic_forms:
            for element in tuple:
                if "subst:sg:nom" in element:
                    result = tuple[0]
    elif case == 'gen':
        for tuple in list_of_morphosyntactic_forms:
            for element in tuple:
                if "subst:sg:gen" in element:
                    result = tuple[0]
    elif case == 'dat':
        for tuple in list_of_morphosyntactic_forms:
            for element in tuple:
                if "subst:sg:dat" in element:
                    result = tuple[0]
    elif case == 'acc':
        for tuple in list_of_morphosyntactic_forms:
            for element in tuple:
                if "subst:sg:nom.acc" in element:
                    result = tuple[0]
                elif "subst:sg:acc" in element:
                    result = tuple[0]
    elif case == 'inst':
        for tuple in list_of_morphosyntactic_forms:
            for element in tuple:
                if "subst:sg:inst" in element:
                    result = tuple[0]
    elif case == 'loc':
        for tuple in list_of_morphosyntactic_forms:
            for element in tuple:
                if "subst:sg:loc" in element:
                    result = tuple[0]
    return result

#Test funkcji
"""
print(Decline_Noun("karczoch", "loc"))
print(Decline_Noun("książka", "acc"))
"""

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


def DeleteTags(keyword):
    new_keyword = keyword.replace('<subst>', "").replace('</subst>', ""). replace('<adj>', "").replace('</adj>', "")
    return new_keyword

# FINDING KEYWORDS IN THE TEXT
#TODO : Dodać tekst
text  ="""
Zamontować cewnik na <subst>endoskop</subst>. Przygotować <subst>endoskop</subst>.
Przysunąć przedmiot do <subst>teleskop</subst>.
Położyć przy <subst>endoskop</subst> lub przed <subst>endoskop</subst> lub
nad <subst>endoskop</subst> lub też pod <subst>endoskop</subst>.
Bez <subst>endoskop</subst>. Przerwa.
Trzymać daleko od <subst>endoskop</subst>.
<subst>książka</subst> leżała na stole. Włożyłam zakładkę do <subst>książka</subst>.
"""

#Regex

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

# Pronoms
pronoms_gen = ["bez", "blisko", "dla", "do", "dookoła", "koło", "mimo", "naokoło", "obok", "od", "ode", "około",\
               "oprócz", "prócz", "podczas", "podług", "pomimo", "poniżej", "pośrodku", "pośród", "powyżej", "spod",\
               "spomiędzy", "sponad", "spośród", "spoza", "sprzed", "u", "według", "wobec", "wokoło", "wokół",\
               "wskutek", "wśród", "wzdłuż", "zamiast", "znad", "zza", "naprzeciw", "naprzeciwko"]
pronoms_dat = ["dzięki", "ku", "przeciw", "przeciw", "wbrew"]
pronoms_acc = ["przez"]
pronoms_inst = []
pronoms_loc = ["przy"]
# Decline words inside list:

for index in list_of_indexes:
    print(index)
    print(list_of_words[index])
#genitif
    if list_of_words[index - 1].lower() in pronoms_gen:
        list_of_words[index] = DeleteTags(list_of_words[index])
        list_of_words[index] = Decline_Noun(list_of_words[index], 'gen')
#datif
    elif list_of_words[index - 1].lower() in pronoms_dat:
        list_of_words[index] = DeleteTags(list_of_words[index])
        list_of_words[index] = Decline_Noun(list_of_words[index], 'dat')
#accusatif
    elif list_of_words[index - 1].lower() in pronoms_acc:
        list_of_words[index] = DeleteTags(list_of_words[index])
        list_of_words[index] = Decline_Noun(list_of_words[index], 'acc')
#instrumental
    elif list_of_words[index - 1].lower() in pronoms_inst:
        list_of_words[index] = DeleteTags(list_of_words[index])
        list_of_words[index] = Decline_Noun(list_of_words[index], 'inst')
#locatif
    elif list_of_words[index - 1].lower() in pronoms_loc:
        list_of_words[index] = DeleteTags(list_of_words[index])
        list_of_words[index] = Decline_Noun(list_of_words[index], 'loc')
    else:
        list_of_words[index] = DeleteTags(list_of_words[index])
        list_of_words[index] = Decline_Noun(list_of_words[index], 'nom')

print(list_of_words)

#TODO Funkcja odmieniająca przymiotniki