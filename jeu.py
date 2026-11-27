"""Les règles du jeu, communes au joueur humain (jalon 1) et à l'agent (jalon 2)."""
import time

from personnage import Personnage
from guerrier import Guerrier
from monstre import BESTIAIRE, creer_monstre
from labyrinthe import Labyrinthe, MUR, POTION


def combat(heros: Personnage, monstre: Personnage, pause: float = 0.0) -> bool:
    """Combat automatique au tour par tour : le héros frappe, puis le monstre riposte
    s'il est encore vivant, jusqu'à ce que l'un des deux meure. On affiche chaque coup.
    Retourne True si le héros a gagné.
    `pause` : nombre de secondes d'attente entre deux tours (time.sleep), utile pour l'agent.
    Pour un Guerrier, affichez le calcul de l'armure, par exemple :
        Gobelin riposte : 3 dégâts - 2 bloqués par l'armure = 1 PV perdus -> Conan (39/40 PV)
    (isinstance(heros, Guerrier) dit si le héros est un Guerrier ; get_armure() donne son armure)."""
    print(f"*** {heros.get_nom()} affronte : {monstre} ! ***")
    # À COMPLÉTER
    pass


def entrer_case(heros: Personnage, labyrinthe: Labyrinthe, position: tuple[int, int],
                pause: float = 0.0) -> bool:
    """Le héros veut entrer dans la case `position`. Applique les règles et retourne True
    s'il est entré dans la case :
    - mur : afficher « Aïe, un mur ! », il n'entre pas ;
    - monstre (symbole dans BESTIAIRE) : combat ; s'il gagne, la case est vidée et il entre ;
    - potion : il la boit, la case est vidée, il entre ;
    - sinon (couloir, sortie) : il entre."""
    l, c = position
    case = labyrinthe.get_case(l, c)
    # À COMPLÉTER
    pass
