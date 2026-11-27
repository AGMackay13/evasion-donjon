"""JALON 2 : un nœud de l'arbre des chemins (même idée que les nœuds d'arbre du TD9-10,
mais avec une LISTE d'enfants au lieu d'un fils gauche et d'un fils droit)."""


class Noeud:
    """Une case du labyrinthe, son parent (la case d'où l'on vient) et ses enfants
    (les cases où l'on peut aller ensuite). La racine est le départ : son parent vaut None."""

    def __init__(self, position: tuple[int, int], parent: "Noeud | None" = None) -> None:
        self._position: tuple[int, int] = position
        self._parent: Noeud | None = parent
        self._enfants: list[Noeud] = []

    def get_position(self) -> tuple[int, int]:
        return self._position

    def get_parent(self) -> "Noeud | None":
        # À COMPLÉTER
        pass

    def get_enfants(self) -> list["Noeud"]:
        # À COMPLÉTER
        pass

    def ajouter_enfant(self, enfant: "Noeud") -> None:
        # À COMPLÉTER
        pass

    def profondeur(self) -> int:
        """Nombre de pas depuis la racine : 0 pour la racine, sinon 1 + la profondeur du parent (récursif !)."""
        # À COMPLÉTER
        pass
