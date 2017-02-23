# -*- coding: utf-8 -*-
## Librairie destiné a l'export de texte dans un fichier texte.

def ecrireFichier(tableau):
	fichier = open('fichier_export.txt', 'w')
	for ligne in tableau:
		for colonne in ligne:
			fichier.write(str(colonne))
		fichier.write('\n')
	fichier.close()

def lireFichier():
	fichier = open('fichier_import.txt', 'r')

ecrireFichier([[5,6,568,89565],[584,4848,165]])
