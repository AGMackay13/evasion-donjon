"""JALON 2 : un agent qui connaît toute la carte et joue tout seul (toujours un Guerrier)."""
import math
import time

from guerrier import Guerrier
from monstre import BESTIAIRE, creer_monstre
from labyrinthe import Labyrinthe, POTION, SORTIE
from jeu import entrer_case
from noeud import Noeud


class Agent:
    def __init__(self, heros: Guerrier, labyrinthe: Labyrinthe) -> None:
        self._heros: Guerrier = heros
        self._labyrinthe: Labyrinthe = labyrinthe

    def construire_arbre(self, eviter: str = "") -> Noeud:
        """Construit l'arbre des chemins, niveau par niveau, à partir du départ (la racine).
        Chaque case n'apparaît qu'UNE fois dans l'arbre (voir le pseudo-code dans le sujet).
        Étape 6 : les cases dont le symbole est dans `eviter` sont traitées comme des murs."""
        racine = Noeud(self._labyrinthe.get_depart())
        deja_dans_arbre: list[tuple[int, int]] = [racine.get_position()]
        file: list[Noeud] = [racine]          # la file du TD9-10 : enfiler = append, défiler = pop(0)
        # À COMPLÉTER
        return racine

    def chercher_sortie(self, racine: Noeud) -> Noeud | None:
        """Parcours en largeur de l'arbre, comme affichage_largeur() au TD9-10, mais au lieu d'afficher
        chaque nœud, on s'arrête au premier nœud qui est sur la SORTIE et on le retourne.
        None si la sortie n'est pas dans l'arbre."""
        # À COMPLÉTER
        pass

    def plus_court_chemin(self, eviter: str = "") -> list[tuple[int, int]]:
        """Construit l'arbre, cherche le nœud de la sortie, puis remonte de parent en parent
        jusqu'à la racine. Retourne la liste des positions, du départ à la sortie ([] si pas de chemin)."""
        # À COMPLÉTER
        return []

    def suivre(self, chemin: list[tuple[int, int]], pause: float = 0.2) -> None:
        """Joue le chemin pour de vrai, case par case, avec entrer_case() (les mêmes règles que le joueur),
        en affichant toute la carte à chaque pas (time.sleep(pause) pour avoir le temps de voir).
        S'arrête si le héros meurt ou atteint la sortie."""
        # À COMPLÉTER
        pass

    # ---------------- Étape 6 : le chemin sûr ----------------

    def pertes_au_pire(self, symbole: str) -> int:
        """PV perdus par le guerrier contre ce monstre si le monstre frappe toujours au maximum.
        Le guerrier frappe en premier : il lui faut tours = math.ceil(pv_du_monstre / force) coups,
        donc le monstre riposte (tours - 1) fois, de (degats_max - armure) à chaque fois (jamais négatif).
        Exemple : contre un Dragon -> 35."""
        monstre = creer_monstre(symbole)
        # À COMPLÉTER
        pass

    def pv_au_pire(self, chemin: list[tuple[int, int]]) -> int:
        """PV restants à la sortie si on suit ce chemin « au pire » :
        un monstre enlève ses pertes au pire, une potion rend 15 PV (sans dépasser le maximum).
        Retourne 0 si le guerrier meurt en route."""
        # À COMPLÉTER
        pass
