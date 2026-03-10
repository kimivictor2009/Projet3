'''
==================== KOVALENT ====================

Bandeau d'informations - tenir à jour !

Version : 1.6

Dernière édition : Victor, 10/03/2025, 16:02


---------- COMMENTAIRE ----------

J'ai trouvé un moyen de dessiner les atomes et liaisons,
mais c'était juste pour remplir la fonction render
Je l'ai supprimé pour faire le menu
J'ai mis tous les noms de trucs en anglais
La variable tick augmente de 1 à chaque frame, pour faire des animations


---------- NOTES ----------

    Note pour le stockage des atomes :
        atomes = [{id : 3, nom : "C", pos : (x=127, y=208), liaisons : [(id=5, nb_liaisons=2), (etc)]}, {atome2}, {etc}]

        type(atomes) = list[dict(int, str, tuple[int, int], list[tuple(int, int)])]

        liste des atomes
        atome = dictionnaire avec infos
        infos = id, formule, position et liaisons
    
    Penser à nommer les variables en anglais pour la réutilisation
    Penser aussi aux docstrings et aux commentaires
    Pas besoin de faire *SCALE pour du texte, la fonction le fait automatiquement
    Pas besoin de scale pour les boutons non plus


---------- HISTORIQUE DES MODIFICATIONS ----------

=> VERSION 1
    -> Version 1.0, Victor
        - Création d'une fenêtre avec pygame
        - Frame dans la fenêtre de dimensions HEIGHT, WIDTH
    -> Version 1.1, Victor
        - Fonction render() pour tester
        - Affichage atomes et liaisons (TEST, sera supprimé)
    -> Version 1.2, Victor
        - Fonctions create_text() et print_text(), permettant d'afficher du texte dans la fenêtre
        - Structuration du code
    -> Version 1.3
        - Dimensionnage automatique de la fenêtre, qui s'adapte à l'écran principal
        - Variable fenetre_basique à changer pour avoir une fenêtre de dimension prédéfinie (pour les devs)
    -> Version 1.4
        - Ajout d'un ticker
        - Ajout d'une intro
        - Ajout d'un titre du menu
    -> Version 1.5
        - Police de caractère style futuriste
    -> Version 1.6
        - Fonction permettant de faire des boutons
        - Bouton "Jouer" (non fonctionnel, test)

==================== main.py ====================
'''


# -----<===== INITIALISATION =====>-----

# ----- Modules importés -----

from __future__ import annotations
import pygame as pg
from screeninfo import get_monitors

# ----- Couleurs, constantes et variables/tableaux/autres -----

fenetre_basique = True
skip_intro = False

if skip_intro :
    tick = 200
else :
    tick = 0

# Test pour une molécule de CH2O (chaque ligne est un atome)
atoms = [{"id" : 1, "name" : "C", "pos" : (127, 208), "links" : [(2, 2), (3, 1), (4, 1)]},
          {"id" : 2, "name" : "O", "pos" : (94, 215), "links" : [(1, 2)]},
          {"id" : 3, "name" : "H", "pos" : (131, 249), "links" : [(1, 1)]},
          {"id" : 4, "name" : "H", "pos" : (134, 157), "links" : [(1, 1)]}]


BLACK = (0, 0, 0)
DARK_GREY = (100, 100, 100)
WHITE = (255, 255, 255)
YELLOW = (200, 200, 0)


# ----- Initialisation de pygame et création de la fenêtre -----


WINDOW_HEIGHT = 700
WINDOW_LENGHT = 1050

PROP_WINDOW = 1.5  # la proportion de la longueur sur la hauteur

if not fenetre_basique :
    # Parcoure les moniteurs et prend le principal
    for m in get_monitors() :
        if m.is_primary : # Le moniteur principal
        
            if (m.height - 150)*1.5 <= m.width : # Si la fenêtre est assez large par rapport à ce qu'on veut si on prend la hauteur en modèle
            
                WINDOW_HEIGHT = m.height - 150 # le 150 est une distance entre le bord haut et bas et la fenêtre
                WINDOW_LENGHT = WINDOW_HEIGHT * PROP_WINDOW
            
            else :  # Sinon
             
                WINDOW_LENGHT = m.width - 50
                WINDOW_HEIGHT = WINDOW_LENGHT / PROP_WINDOW
    


SCALE = WINDOW_HEIGHT/800
# Correspond à la taille de la fenêtre, tout doit être proportionnel
# SCALE vaut 1.0 si la fenêtre à une hauteur (par défaut) de 800px, ce qui correspond à celle de fenetre_basique
# ATTENTION C'EST UN FLOAT
# Pas besoin de faire *SCALE pour du texte, la fonction le fait automatiquement



WINDOW_SIZE = (WINDOW_LENGHT, WINDOW_HEIGHT)

pg.init()

surface = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption("Kovalent")

# ----- Fonts -----

pg.font.init()
fichier_font = pg.font.get_default_font() #"data/super_font.otf"

def create_text(text : str, size : int, color : tuple = WHITE) -> pg.Surface :
    '''Renvoie une Surface de texte, à blit pour afficher'''
    
    font = pg.font.Font(fichier_font, size)
    return font.render(text, True, color)


def print_txt(text : str, pos : tuple, size : int = 30, color : tuple = WHITE, center : bool=False, dest = surface) -> None :
    '''Affiche du texte dans la fenêtre, mis automatiquement à son échelle'''
    
    s = create_text(text, int(size*SCALE), color)
    if center :
        dest.blit(s, (int(pos[0]*SCALE)-s.get_width()/2, int(pos[1]*SCALE)-s.get_height()/2.5))
    else :
        dest.blit(s, (int(pos[0]*SCALE), int(pos[1]*SCALE)))


# -----<===== FONCTIONS PRINCIPALES =====>-----


def render() -> None :
    '''Affiche tout ce qu'il faut afficher à l'écran'''
    
    # Les 200 premiers ticks sont pour une petite intro
    
    if tick < 200 :
        if tick < 20 :
            surface.fill(BLACK)
        elif tick <= 80 :
            surface.fill(BLACK)
            teinte = ((tick-20)/60)*255
            print_txt("KVTeam", (600, 350), 50, (teinte, teinte, teinte), True)
        elif tick >= 170 :
            surface.fill(BLACK)
            teinte = (1-((tick-170)/30))*255
            print_txt("KVTeam", (600, 350), 50, (teinte, teinte, teinte), True)
    else :
        surface.fill(DARK_GREY)
        main_menu()



def main_menu() -> None :
    '''Affiche le menu principal'''
    if tick < 300 :
        print_txt("KOVALENT", (600, 100), 70, WHITE, True)
    else :
        print_txt("KOVALENT", (600, 100), 70, WHITE, True)
    
    button((450, 300, 300, 100), "Jouer", BLACK, 50, WHITE, DARK_GREY)


def button(rect : tuple, text : str, text_color : tuple, text_size : int, color : tuple, color2 : tuple) -> bool :
    '''Affiche un bouton à rect(gauche, haut, longueur, hauteur),
    du texte, avec couleur et taille, et sa couleur, et renvoie True si il est cliqué.
    Il passe à la couleur de color2 (optionnel) quand la souris est dessus'''
    
    rleft = rect[0]
    rtop = rect[1]
    rwidth = rect[2]
    rheight = rect[3]
    
    mp = pg.mouse.get_pos()
    mpx = mp[0]
    mpy = mp[1]
    
    if mpx >= rleft*SCALE and mpy >= rtop*SCALE and mpx <= (rleft + rwidth)*SCALE and mpy <= (rtop + rheight)*SCALE :
        pg.draw.rect(surface, color2, (rleft*SCALE, rtop*SCALE, rwidth*SCALE, rheight*SCALE))
        print_txt(text, ((rleft + (rwidth/2)), (rtop + (rheight/2))), text_size, text_color, True)
        return True
    else :
        pg.draw.rect(surface, color, (rleft*SCALE, rtop*SCALE, rwidth*SCALE, rheight*SCALE))
        print_txt(text, ((rleft + (rwidth/2)), (rtop + (rheight/2))), text_size, text_color, True)
        return False
    
    
    

# -----<===== BOUCLE PRINCIPALE =====>-----


clock = pg.time.Clock()

running = True

while running == True :
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False   # Quitte la boucle quand l'évènement QUIT est détecté
    
    
    render()
    pg.display.flip()
    
    tick += 1 # + 1 ticks par frame (60 par seconde)
    clock.tick(60) # Met le FPS à 60
    
pg.quit()


