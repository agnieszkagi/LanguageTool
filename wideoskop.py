#! python3
import re

text  ="""
Zamontować cewnik na wideoskop. Przygotować wideoskop. Przysunąć przedmiot do wideoskop.
Położyć przy wideoskop lub przed wideoskop lub nad wideoskop lub też pod wideoskop. Bez wideoskop.
Trzymać daleko od wideoskop.
"""
word ="wideoskop" #<subst:sg:nom:m1>

#deklinacja r.m. l.poj. nieżywotne typ 1

mianownik = ""
dopełniacz = "u"
celownik ="owi"
biernik = mianownik
narzędnik ="em"
miejscownik ="ie"

Regex = re.compile(r'\s\w+\swideoskop') #TODO dodać jeszcze spację/kropkę/przecinek na końcu, żeby nie odmieniać już odmienionych rzeczowników
list = Regex.findall(text)
print(Regex.findall(text))

for element in list:
    if element.lower().startswith(" do ") or element.lower().startswith(" od ") or element.lower().startswith(" bez "):
        text=text.replace(element, element+dopełniacz)
    elif element.lower().startswith(" na ") or element.lower().startswith(" przy "):
        text = text.replace(element, element + miejscownik)
    elif element.lower().startswith(" nad ") or element.lower().startswith(" pod ") or element.lower().startswith(" przed "):
        text = text.replace(element, element + narzędnik)
#text.replace("przy "+word, "przy "+word+miejscownik )
print(text)