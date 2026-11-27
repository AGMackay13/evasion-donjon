"""L'Évasion du Donjon - point d'entrée du jeu : python main.py"""
from personnage import Personnage
from guerrier import Guerrier
from archer import Archer
from magicien import Magicien
from labyrinthe import Labyrinthe, DIRECTIONS, SORTIE
from jeu import entrer_case
# from agent import Agent          # jalon 2 : enlever le # au début de cette ligne


def choisir(question: str, reponses: list[str]) -> str:
    """Pose la question jusqu'à obtenir une des réponses autorisées (fourni)."""
    choix = ""
    while choix not in reponses:
        choix = input(question).strip().lower()
    return choix


def choisir_heros() -> Personnage:
    """Demande la classe et le nom du héros, et le crée.
    Héros conseillés : Guerrier(nom, 40, 6), Archer(nom, 40, 0.85, 15), Magicien(nom, 30, 40)."""
    choix = choisir("Votre héros : 1. Guerrier   2. Archer   3. Magicien\n> ", ["1", "2", "3"])
    nom = input("Son nom : ").strip()
    # À COMPLÉTER
    pass


def jouer(heros: Personnage, labyrinthe: Labyrinthe, debug: bool) -> None:
    """Jalon 1 : la boucle de jeu, le joueur se déplace à la main.
    Tant que le héros est vivant :
      - afficher la vue du héros (labyrinthe.decrire) ou, en mode debug, toute la carte (labyrinthe.afficher),
        puis le héros (print(heros)) ;
      - lire une touche : choisir("Déplacement (z/q/s/d), x pour quitter : ", list(DIRECTIONS) + ["x"]) ;
      - calculer la case de destination grâce à DIRECTIONS, puis appeler entrer_case() ;
      - si le héros est entré : il change de position ; si c'est la SORTIE -> VICTOIRE !
    Si le héros meurt : GAME OVER."""
    position = labyrinthe.get_depart()
    # À COMPLÉTER


def main() -> None:
    print("=== L'Évasion du Donjon ===")
    mode = choisir("1. Jouer   2. Jouer (mode debug)\n> ", ["1", "2"])
    # Jalon 2 : ajouter au menu  3. Agent : plus court chemin   4. Agent : chemin sûr
    niveau = choisir("Niveau 1 ou 2 ? ", ["1", "2"])
    if niveau == "1":
        labyrinthe = Labyrinthe("niveaux/niveau1.txt")
    else:
        labyrinthe = Labyrinthe("niveaux/niveau2_piege.txt")
    if mode in ("1", "2"):
        jouer(choisir_heros(), labyrinthe, debug=(mode == "2"))


if __name__ == "__main__":
    main()
