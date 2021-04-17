# L'interface graphique avec Tkinter

> Début

## Guide de l'utilisation de l'interface graphique

L'interface possède le menu, le canvas, où se passe la construction 
des figures et leur modification et le menu de styles, à droite de canvas pour
stylisé des figures et contrôlé leur position


### Menu 

`File` : contient le bouton `exit` pour sortir de l'interface

`Figure` : est utilisé pour choisir une figure (Point, Triangle ou Cercle)

### Canvas

Canvas est utilisé pour déssiner, déplacer et modifier des figures à la main

`Mouse-Left-Click` : est utilisé pour créer une figure ayant le point clické comme barycentre

`Mouse-Right-Click` : est utilisé pour supprimer la figure

`Shift + Mouse-Left-Click` : est utilisé pour déplacer une figure déjà existante

### Menu de styles

Affiche les coordonnées de la position de curseur sur le canvas.

## La structure de code

Le projet contient des fichiers suivants

1. [fichier principal](#fichier-principal)
2. [figures](#figures)
3. [listeners](#listeners)
4. [managers](#managers)
5. [widgets](#widgets)


### Fichier principal

***

### Figures

Ce dossier contient des classes de figures géometriques (Point, Cercle et Triangle)

#### Point

`x : absisse de point`

`y : ordonné de point`

`canvas_object : objet tkinter correspondant (en realité l'id)`

`set_point(x,y) : change les coordonnées de point`

`set_coordinates(x,y) : même chose, mais c'est un méthode présent dans toutes les classes de figures`

`get_coordinates() : renvoie les coordonnées de point`

`set_canvas_object(canvas_object) : change la valeur de canvas_object`

`distance(point) : renvoie la distance entre ce point et le point passé en paramètres`

#### Circle

#### Triangle


***

### Listeners

contient lui-même 2 dossiers : `draw-listeners` et `interface_listeners`

#### draw_listeners

#### interface_listeners

***

### Managers

***

### Widgets

Ce dossier contient tous les éléments de l'interface graphique d'utilisateur.

#### ProgramMenu.py

C'est un menu que l'utilisateur voit en haut de l'onglet du logiciel.

#### StyleMenu.py

C'est le menu de styles, que l'utilisateur voit à droite de canvas en haut de l'onglet. 
Ce menu permet de changer la couleur de remplissage, ainsi que la couleur de bord. Ce menu
est aussi utilisé pour afficher les coordonnées de curseur sur le canvas.

> Fin
