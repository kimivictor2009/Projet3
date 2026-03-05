'''

==================== KOVALENT ====================


---------- NOTES ----------
    Note pour le stockage des atomes :
        atomes = [{id : 3, nom : "C", pos : (x=127, y=208), liaisons : [(id=5, nb_liaisons=2), (etc)]}, {atome2}, {etc}]

        type(atomes) = list[dict(int, str, tuple[int, int], list[tuple(int, int)])]

        liste des atomes
        atome = dictionnaire avec infos
        infos = id, formule, position et liaisons

---------- HISTORIQUE DES MODIFICATIONS ----------

-> VERSION 1.0
    - Création d'une fenêtre avec pygame
    - Frame dans la fenêtre de dimensions HEIGHT, WIDTH


==================== main.py ====================

'''

# -----<===== INITIALISATION =====>-----

# ----- Modules importés -----

from __future__ import annotations
import pygame as pg


# ----- Couleurs, constantes et initialisation de pygame -----

# Test pour une molécule de CH2O
atomes = [{"id" : 1, "nom" : "C", "pos" : (127, 208), "liaisons" : [(2, 2), (3, 1), (4, 1)]},
          {"id" : 2, "nom" : "O", "pos" : (94, 215), "liaisons" : [(1, 2)]},
          {"id" : 3, "nom" : "H", "pos" : (131, 249), "liaisons" : [(1, 1)]},
          {"id" : 4, "nom" : "H", "pos" : (134, 157), "liaisons" : [(1, 1)]}]



GREY = (180, 180, 180)
DARK_WHITE = (238, 238, 213)
GREEN = (125, 148, 93)
BG_GREY = (150, 150, 150)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (160, 130, 110)


SCALE = 100 # Taille de la fenêtre en %, tout doit être proportionnel - peut être modifié à volonté

WINDOW_LENGHT = SCALE*6
WINDOW_HEIGHT = SCALE*6

WINDOW_SIZE = (WINDOW_LENGHT, WINDOW_HEIGHT)

surface = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption("Kovalent")