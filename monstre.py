import random

from personnage import Personnage


class Monstre(Personnage):
    """Un monstre inflige des dégâts aléatoires entre degats_min et degats_max."""

    def __init__(self, nom: str, pv: int, degats_min: int, degats_max: int) -> None:
        # À COMPLÉTER
        pass

    def get_degats_max(self) -> int:
        # À COMPLÉTER
        pass

    def attaquer(self) -> int:
        # À COMPLÉTER : un nombre entier au hasard entre degats_min et degats_max -> random.randint(a, b)
        pass


# Le bestiaire : symbole sur la carte -> (nom, PV, dégâts min, dégâts max)
BESTIAIRE: dict[str, tuple[str, int, int, int]] = {
    "G": ("Gobelin", 10, 1, 4),
    "K": ("Squelette", 15, 2, 6),
    "D": ("Dragon", 35, 4, 9),
}


def creer_monstre(symbole: str) -> Monstre:
    """Crée le monstre correspondant à un symbole de la carte. Exemple : creer_monstre("G") -> un Gobelin."""
    nom, pv, degats_min, degats_max = BESTIAIRE[symbole]
    return Monstre(nom, pv, degats_min, degats_max)
