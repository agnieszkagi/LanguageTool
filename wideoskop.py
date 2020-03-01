#! python3
import re

text  ="""
Zamontować cewnik na endoskop. Przygotować endoskop. Przysunąć przedmiot do endoskop.
Położyć przy wideoskop lub przed endoskop lub nad endoskop lub też pod endoskop. Bez endoskop.
Trzymać daleko od endoskop.
"""
word ="endoskop|gen:u|dat:owi|acc:|inst:em|loc:ie|" #<subst:sg:nom:m1>

#deklinacja r.m. l.poj. nieżywotne typ 1

nom = ""
gen = "u"
dat ="owi"
acc = nom
inst ="em"
loc ="ie"

Regex = re.compile(r'\s\w+\sendoskop') #TODO dodać jeszcze spację/kropkę/przecinek na końcu, żeby nie odmieniać już odmienionych rzeczowników
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