from personnage import Personnage


class Magicien(Personnage):
    """Lance une boule de feu (12 dégâts, coûte 5 de mana). Sans assez de mana : coup de bâton (2 dégâts)."""

    def __init__(self, nom: str, pv: int, mana: int) -> None:
        # À COMPLÉTER : attributs _mana et _mana_max (le mana de départ est aussi le maximum)
        pass

    def get_mana(self) -> int:
        # À COMPLÉTER
        pass

    def attaquer(self) -> int:
        # À COMPLÉTER
        pass

    def boire_potion(self) -> None:
        # À COMPLÉTER : comme tout le monde (appeler la méthode du parent)... ET le mana revient au maximum
        pass

    def __str__(self) -> str:
        # Exemple : "Merlin (30/30 PV) [40 mana]"
        # À COMPLÉTER
        pass
