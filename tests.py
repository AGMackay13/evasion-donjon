"""Tests : lancer « python tests.py ». À compléter avec VOS propres tests (au moins un par classe)."""
from guerrier import Guerrier
from magicien import Magicien

conan = Guerrier("Conan", 40, 6)
conan.subir_degats(5)
assert conan.get_pv() == 37       # l'armure a absorbé 2 dégâts
conan.subir_degats(1)
assert conan.get_pv() == 37       # jamais de dégâts négatifs !
assert conan.attaquer() == 6

merlin = Magicien("Merlin", 30, 12)
assert merlin.attaquer() == 12 and merlin.attaquer() == 12
assert merlin.attaquer() == 2     # plus assez de mana : coup de bâton
merlin.boire_potion()
assert merlin.get_mana() == 12

# À COMPLÉTER : des tests pour Archer, Monstre, Labyrinthe...

# Jalon 2 : enlever les # devant les lignes suivantes
# from labyrinthe import Labyrinthe
# from agent import Agent
# agent = Agent(Guerrier("Agent", 40, 6), Labyrinthe("niveaux/niveau2_piege.txt"))
# assert agent.pertes_au_pire("D") == 35
# sortie = agent.chercher_sortie(agent.construire_arbre())
# assert sortie is not None and sortie.profondeur() == 20   # la sortie est à 20 pas de la racine
# assert len(agent.plus_court_chemin()) - 1 == 20      # 20 pas

print("Tous les tests sont passés !")
