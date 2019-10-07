#!/usr/bin/python3


def getNbCoursesSemaine() :
	
	# Compléter le code
	
	
	for numJour in range( 1 , 8 ) :
		
		msg = "Nombre de courses réalisées le jour " + str( numJour ) + " : "
		
		nbCourses = input( msg )

	
	
	
	

if __name__ == "__main__" :
	
	nbCourses = getNbCoursesSemaine()
	print( "Cette semaine, vous avez affectué" , nbCourses , "courses." )
