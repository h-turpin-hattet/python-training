#Exercices sur list compréhension !

#Exercice 1:
#Crée une nouvelle liste avec uniquement les nombres pairs.
def list_pair(nombres):
    return [i for i in nombres if i%2==0]

nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_pair(nombres))


#Exercice 2:
#Crée une nouvelle liste avec tous les mots en majuscules.
def list_maj_expended(mots):
    result = []
    for i in mots:
        result.append(i.upper())


    return result

def list_maj(mots):
    return [i.upper() for i in mots]

mots = ["hello", "world", "python", "codewars"]
mots2 = ["hello", "world", "python", "codewars"]
print(list_maj(mots))
print (list_maj_expended(mots2))


#Exercice 3:
#Crée une nouvelle liste avec le carré des nombres positifs uniquement.
def list_square_positive(nombres):
    return [i**2 for i in nombres if i>0]

def list_square_positive_extended(nombres):
    result=[]
    for i in nombres:
        if i>0:
            result.append(i**2)

    return result

nombres = [-3, -2, -1, 0, 1, 2, 3]
nombres2 = [-3, -2, -1, 0, 1, 2, 3]
print(list_square_positive(nombres))
print(list_square_positive_extended(nombres2))
