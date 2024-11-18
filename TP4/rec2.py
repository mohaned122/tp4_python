class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# Fonction récursive pour vérifier si la liste est un palindrome
def verifier_palindrome(tête):
    def helper(nœud):
        nonlocal début
        if nœud is None:  # Condition d'arrêt pour atteindre la fin de la liste
            return True
        # Appel récursif pour avancer jusqu'à la fin
        if not helper(nœud.next):
            return False
        # Comparaison lors du retour de la récursion
        is_palindrome = (début.value == nœud.value)
        début = début.next  # Avancer le pointeur de début
        return is_palindrome

    début = tête  # Initialiser le pointeur de début
    return helper(tête)


# Création des nœuds de la liste palindrome : A -> C -> I -> V -> I -> C -> A
nœud1 = Node('A')
nœud2 = Node('B')
nœud3 = Node('I')
nœud4 = Node('V')
nœud5 = Node('I')
nœud6 = Node('B')
nœud7 = Node('A')

# Liaison des nœuds
nœud1.next = nœud2
nœud2.next = nœud3
nœud3.next = nœud4
nœud4.next = nœud5
nœud5.next = nœud6
nœud6.next = nœud7

# Vérification si la liste est palindrome
if verifier_palindrome(nœud1):
    print("La liste est un palindrome.")
else:
    print("La liste n'est pas un palindrome.")
