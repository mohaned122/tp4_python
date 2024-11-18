class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def afficher_liste_recursive(noeud):
    if noeud is None:  # Condition d'arrêt
        return
    else:
        print(noeud.value)
        afficher_liste_recursive(noeud.next)

def plindrom(nœud):
    if nœud is None:  # Condition d'arrêt
        return
    else:
        droit = nœud.value
        plindrom(nœud.next)
        gauche = nœud.value
        if droit != gauche:
            return False

    return True

# Exemple d'utilisation
# Création des nœuds
nœud1 = Node(1)
nœud2 = Node(2)
nœud3 = Node(3)

# Liaison des nœuds
nœud1.next = nœud2
nœud2.next = nœud3

# Appel de la fonction
afficher_liste_recursive(nœud1)
print(plindrom(nœud1))
