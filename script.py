import sys
from shutil import copyfile

def main():
	mon_fichier = open("fichier.txt", "w")
	mon_fichier.write(sys.argv[1] + " traite")
	copyfile(""+sys.argv[1],"/static/img/"+sys.argv[1])
	


main()
