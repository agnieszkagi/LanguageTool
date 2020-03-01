#! python3
import re

glossary = ["<subst>endoskop||u|owi||em|ie</subst>", "<subst>teleskop||u|owi||em|ie</subst>", "<subst>książ|ka|ki|ce|kę|ką|ce</subst>" ]
# FUNKCJE ODMIENIAJĄCE TERMINY SŁOWNIKOWE WEDŁUG PRZYPADKW I ZWRACAJĄCE KOŃCÓWKĘ
# nominative (mianownik)
def nom(keyword):
    endings = keyword.split("|")
    result = endings[0]+endings[1]
    return result
# genitive (dopełniacz)
def gen(keyword):
    endings = keyword.split("|")
    result = endings[0]+endings[2]
    return result
# dative (celownik)
def dat(keyword):
    endings = keyword.split("|")
    result = endings[0]+endings[3]
    return result
# accusative (biernik)
def acc(keyword):
    endings = keyword.split("|")
    result = endings[0]+endings[4]
    return result
# instrumental (narzędnik)
def inst(keyword):
    endings = keyword.split("|")
    result = endings[0]+endings[5]
    return result
# locative (miejscownik)
def loc(keyword):
    endings = keyword.split("|")
    result = endings[0]+endings[6]
    return result

print(nom(glossary[2]))
print(gen(glossary[2]))
print(dat(glossary[2]))
print(acc(glossary[2]))
print(inst(glossary[2]))
print(loc(glossary[2]))

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
Regex = re.compile(r'\s\S+\s+<subst>\S+</subst>')
list = Regex.findall(text)
print(Regex.findall(text))
"""
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
