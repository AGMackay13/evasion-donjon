from personnage import Personnage


class Guerrier(Personnage):
    """Frappe fort (autant que sa force) et son armure absorbe une partie des coups."""

    def __init__(self, nom: str, pv: int, force: int, armure: int = 2) -> None:
        super().__init__(nom, pv)       # le parent s'occupe du nom et des PV
        self._force: int = force
        self._armure: int = armure

    def get_force(self) -> int:
        return self._force

    def get_armure(self) -> int:
        # À COMPLÉTER
        pass

    def attaquer(self) -> int:
        # À COMPLÉTER : le guerrier inflige autant de dégâts que sa force
        pass

    def subir_degats(self, degats: int) -> None:
        # À COMPLÉTER : l'armure réduit les dégâts de self._armure (jamais de dégâts négatifs !),
        # puis on appelle la méthode du parent : super().subir_degats(...)
        pass
