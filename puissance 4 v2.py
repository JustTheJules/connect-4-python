import random
from tkinter import *

class Pion:
    def __init__(self, colonne, ligne, couleur):
        self.colonne = colonne
        self.ligne = ligne
        if couleur == 1:
            self.couleur = 'red'
        elif couleur == 2:
            self.couleur = 'yellow'

    def afficher(self):
        print(f"Pion de couleur {self.couleur} en colonne {self.colonne} et ligne {self.ligne}")

    def afficher_interface_graphique(self, canvas):
        C = 70
        rayon = 30
        marge = 5
        x = (self.colonne + 0.5) * C
        y = (self.ligne + 0.5) * C
        canvas.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, fill=self.couleur)

class Grille:
    def __init__(self):
        self.pions = [[None] * 7 for _ in range(6)]
        self.dernier_pion = None
        self.derniere_couleur = None

    def ajouter_pion(self, colonne):

        ligne = None
        for i in range(5, -1, -1):
            if self.pions[i][colonne] is None:
                ligne = i
                break

        if ligne is not None:
            if self.derniere_couleur == 'red':
                couleur = 'yellow'
            elif self.derniere_couleur == 'yellow':
                couleur = 'red'
            else:
                couleur = first_couleur
            pion = Pion(colonne, ligne, 1 if couleur == 'red' else 2)
            self.pions[ligne][colonne] = pion
            pion.afficher_interface_graphique(Canevas)
            self.dernier_pion = pion
            if self.verifier_victoire(pion):
                print(f"Victoire pour l'équipe {pion.couleur} !")
                BoutonJouer.config(state=DISABLED)
            else:
                self.derniere_couleur = couleur
                if self.derniere_couleur == 'red':
                    next_turn = 'yellow'
                elif self.derniere_couleur == 'yellow':
                    next_turn = 'red'
                message_next_turn.set(f"Au tour de {next_turn}")
        else:
            print("Cette colonne est pleine.")

    def verifier_victoire(self, pion):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dx, dy in directions:
            count = 1
            for i in range(1, 4):
                x = pion.colonne + dx * i
                y = pion.ligne + dy * i
                if 0 <= x < 7 and 0 <= y < 6 and self.pions[y][x] is not None and self.pions[y][x].couleur == pion.couleur:
                    count += 1
                else:
                    break
            for i in range(1, 4):
                x = pion.colonne - dx * i
                y = pion.ligne - dy * i
                if 0 <= x < 7 and 0 <= y < 6 and self.pions[y][x] is not None and self.pions[y][x].couleur == pion.couleur:
                    count += 1
                else:
                    break
            if count >= 4:
                return True
        return False


def jouer():
    colonne = var_colonne.get()
    grille.ajouter_pion(colonne)


def initialisation():
    C = 70
    for i in range(7):
        for j in range(7):
            Canevas.create_oval(5 + j * C, 5 + i * C, C * (j + 1) - 5, C * (i + 1) - 5, fill="snow")

grille = Grille()

Mafenetre = Tk()
Mafenetre.title('Puissance 4')
Mafenetre.geometry('650x715+20+20')
Largeur = 490
Hauteur = 420
couleur1 = "blue"

Canevas = Canvas(Mafenetre, width=Largeur, height=Hauteur, bg=couleur1)

var_colonne = IntVar()
var_colonne.set(0)

message = StringVar()
message.set("Choisir la colonne : ")
Label(Mafenetre, textvariable=message).pack(padx=1, pady=1)

colonnes_frame = Frame(Mafenetre)
colonnes_frame.pack()

for i in range(7):
    Radiobutton(colonnes_frame, text=str(i+1), variable=var_colonne, value=i).grid(row=0, column=i)

BoutonJouer = Button(Mafenetre, text='Jouer', fg='red', command=jouer)
BoutonJouer.pack(padx=10, pady=10)

message_next_turn = StringVar()
first_couleur= 'red' if random.randint(1, 2) == 1 else 'yellow'
message_next_turn.set(f"Au tour de {first_couleur}")
Label(Mafenetre, textvariable=message_next_turn).pack(padx=1, pady=1)

BoutonQuitter = Button(Mafenetre, text='Quitter', fg='red', command=Mafenetre.destroy)
Canevas.pack(padx=10, pady=10)

BoutonQuitter.pack(side=RIGHT, padx=10, pady=10)
initialisation()
Mafenetre.mainloop()