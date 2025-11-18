"""
Exercice 4 : Liste de courses
 Créez un petit programme avec les fonctions suivantes :
 afficher_liste(courses)
 : affiche tous les articles
 ajouter_article(courses, article)
 : ajoute un article à la liste
 retirer_article(courses, article)
 : retire un article de la liste
 compter_articles(courses)
 : retourne le nombre d'article
 """

# Définission Variable




# Fonction pour afficher la liste des courses
def afficher_liste(course):
    print(course)

# Fonction pour ajouter un article à la liste
def ajouter_article(course, article):
    course.append(article)

# Fonction pour retirer un article de la liste
def retirer_article(course, article):
    #if article in course:
    course.remove(article)

# Fonction pour compter le nombre d'articles dans la liste
def compter_articles(course):
    return len(course)


# Utilisation des fonctions
Liste_Course = ["salade", "tomates"]


print("Dans la liste de course il y à : ")
afficher_liste(Liste_Course) 


Nombre_article = compter_articles(Liste_Course)
ajout_article = ajouter_article(Liste_Course, "fromage")
Retrait_article = retirer_article(Liste_Course, "tomates")


afficher_liste(Liste_Course) 
print(f" soit un total de {Nombre_article} articles ")
print(f" si on ajoute {ajout_article} et qu'on retire {Retrait_article},")
print(f"la nouvelle liste contient {Liste_Course}, pour un total de {Nombre_article} articles.")

