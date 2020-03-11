#! python3
import re
import morfeusz2




def Decline(keyword, case):
    ''' Decline nouns and adjectives '''
    morf = morfeusz2.Morfeusz()
    list_of_morphosyntactic_forms = morf.generate(keyword)
    if case == 'nom':
        for tuple in list_of_morphosyntactic_forms:
            #element.replace("(", "").replace(")", "")
            #list_of_forms = element.split(",")
            for element in tuple:
                if "subst:sg:nom" in element:
                    result = tuple[0]
    return result

print(Decline("endoskop", "nom"))
#dokończę

"""
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
    return result"""