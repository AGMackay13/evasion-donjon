import os

from colorama import Fore, Style, just_fix_windows_console

just_fix_windows_console()   # pour que les couleurs marchent dans le terminal Windows

# Les symboles de la carte
MUR = "#"
VIDE = "."
DEPART = "H"
SORTIE = "S"
POTION = "P"

# touche -> (nom de la direction, déplacement en ligne, déplacement en colonne)
DIRECTIONS: dict[str, tuple[str, int, int]] = {
    "z": ("nord", -1, 0),
    "s": ("sud", 1, 0),
    "q": ("ouest", 0, -1),
    "d": ("est", 0, 1),
}


class Labyrinthe:
    """Une grille de caractères lue dans un fichier texte (voir le dossier niveaux/).
    Une position est un tuple (ligne, colonne) ; la case en haut à gauche est (0, 0)."""

    def __init__(self, chemin_fichier: str) -> None:
        # chemin pris depuis le dossier de ce fichier : marche même si Python est lancé ailleurs
        chemin_fichier = os.path.join(os.path.dirname(os.path.abspath(__file__)), chemin_fichier)
        self._grille: list[list[str]] = []
        with open(chemin_fichier, encoding="utf-8") as fichier:
            for ligne in fichier:
                if ligne.strip() != "":                          # on ignore les lignes vides
                    self._grille.append(list(ligne.rstrip("\n")))  # une ligne = une liste de caractères
        self._depart: tuple[int, int] = (0, 0)
        # À COMPLÉTER : chercher la case DEPART ("H") dans la grille, mémoriser sa position
        # dans self._depart, et la remplacer par un couloir (VIDE)

    def get_depart(self) -> tuple[int, int]:
        return self._depart

    def get_case(self, l: int, c: int) -> str:
        """Le contenu de la case (l, c). En dehors de la grille : on fait comme si c'était un mur."""
        # À COMPLÉTER
        pass

    def vider_case(self, l: int, c: int) -> None:
        """La case devient un couloir (monstre vaincu, potion bue)."""
        # À COMPLÉTER
        pass

    def decrire(self, position: tuple[int, int]) -> None:
        """Vue du héros, qui ne voit que sa case. Exemple d'affichage :
        Vous êtes dans un couloir sombre. Passages : nord (z), sud (s)"""
        # À COMPLÉTER : pour chaque touche de DIRECTIONS, regarder si la case voisine est un mur
        pass

    def afficher(self, position_heros: tuple[int, int]) -> None:
        """Mode debug : toute la carte, en couleur (héros @ en vert, monstres en rouge...)."""
        # À COMPLÉTER. Exemple d'utilisation de colorama :
        #     print(Fore.RED + "G" + Style.RESET_ALL)       # G en rouge, puis retour à la normale
        # Astuce : construire chaque ligne dans une chaîne de caractères, puis l'afficher avec print.
        pass

    # ---------------- Jalon 2 ----------------

    def voisins(self, position: tuple[int, int]) -> list[tuple[int, int]]:
        """Les cases voisines (nord, sud, ouest, est) qui ne sont pas des murs."""
        # À COMPLÉTER au jalon 2
        pass
