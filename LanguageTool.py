#! python3
import re
import morfeusz2

glossary = ["<subst>endoskop||u|owi||em|ie</subst>", "<subst>teleskop||u|owi||em|ie</subst>", "<subst>książ|ka|ki|ce|kę|ką|ce</subst>" ]
# Function decline nouns
morf = morfeusz2.Morfeusz()


"""
def Decline(keyword, case):
    ''' Decline nouns and adjectives '''

    morf = morfeusz2.Morfeusz()
    list_of_morphosyntactic_interpretations = morf.generate(keyword)
    for element in list_of_morphosyntactic_interpretations:
        if case == 'nom':
            list_of_forms = element.split(',')
            for form in list_of_forms():
                if 'subst:sg:nom' in form:
                    result = list_of_forms[0]

print(Decline("teleskop", "nom"))"""
"""

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

"""