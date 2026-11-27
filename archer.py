import random

from personnage import Personnage


class Archer(Personnage):
    """Tire des flèches (10 dégâts si le tir réussit). Sans flèche : coup de dague (2 dégâts)."""

    def __init__(self, nom: str, pv: int, dexterite: float, fleches: int) -> None:
        # À COMPLÉTER (s'inspirer du constructeur de Guerrier)
        # dexterite : probabilité de toucher, dans ]0, 1]
        pass

    def get_fleches(self) -> int:
        # À COMPLÉTER
        pass

    def attaquer(self) -> int:
        # À COMPLÉTER
        # - sans flèche : coup de dague, 2 dégâts
        # - sinon : on consomme une flèche ; le tir touche (10 dégâts) si random.random() < dextérité,
        #   sinon il est raté (0 dégât)
        pass

    def __str__(self) -> str:
        # Exemple : "Robin (40/40 PV) [15 flèches]"  ->  super().__str__() donne déjà le début !
        # À COMPLÉTER
        pass
