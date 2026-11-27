"""Classe abstraite Personnage : tout ce qui combat dans le donjon (héros et monstres).

CE FICHIER EST FOURNI COMPLET : il vous sert de modèle pour écrire les autres classes
(attributs protégés avec _, types explicites, une docstring par classe).
"""
from abc import ABC, abstractmethod


class Personnage(ABC):
    """Un personnage a un nom et des points de vie (PV), jamais négatifs."""

    def __init__(self, nom: str, pv: int) -> None:
        self._nom: str = nom
        self._pv: int = pv
        self._pv_max: int = pv          # les PV de départ sont aussi le maximum

    def get_nom(self) -> str:
        return self._nom

    def get_pv(self) -> int:
        return self._pv

    def get_pv_max(self) -> int:
        return self._pv_max

    def est_vivant(self) -> bool:
        return self._pv > 0

    def subir_degats(self, degats: int) -> None:
        """Les PV ne descendent jamais sous 0."""
        self._pv = max(0, self._pv - degats)

    def soigner(self, soin: int) -> None:
        """Les PV ne dépassent jamais le maximum."""
        self._pv = min(self._pv_max, self._pv + soin)

    def boire_potion(self) -> None:
        """Une potion rend 15 PV."""
        self.soigner(15)

    @abstractmethod
    def attaquer(self) -> int:
        """Retourne le nombre de dégâts infligés (0 si l'attaque échoue).
        Méthode abstraite : chaque sous-classe DOIT la redéfinir."""

    def __str__(self) -> str:
        return f"{self._nom} ({self._pv}/{self._pv_max} PV)"
