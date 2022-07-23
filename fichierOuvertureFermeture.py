# open( )
# close( ) TOUJOURS FERME UN FICHIER SINON IL NE SERA PAS ACCESSIBLE

nom_fichier = open("fichier.txt", "w")
''' 
modes : 
r pour read 
w pour write : dans ce cas le contenu du fichier est ecrase ou 
                le fichier est cree si il n'existe pas.
a pour ouverture en ecriture en mode ajout  
            le fichier est cree si besoin '''
# b pour binaire

nom_fichier.close()