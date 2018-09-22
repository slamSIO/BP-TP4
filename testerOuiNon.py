#!/usr/bin/python3
# coding: utf-8

def saisirOuiNon( question ) :
	pass
	# Votre code ici

if __name__ == "__main__" :
	reponse = saisirOuiNon( "Avez-vous travaillé aujourd'hui ?" )
	if reponse == "oui" :
		print( "Vous avez travaillé aujourd'hui." )
	else :
		print( "Vous n'avez pas travaillé aujourd'hui." )
