import sys
import os
from shutil import copyfile

def main():
    mon_fichier = open("fichier.txt", "w")
    mon_fichier.write(sys.argv[1] + " traite")
    print("./output "+"static/uploads/"+sys.argv[1]+ " "+sys.argv[2] + " "+ sys.argv[3])
    os.system("./output "+"static/uploads/"+sys.argv[1]+ " "+sys.argv[2] + " "+ sys.argv[3])
    copyfile("result.png","static/img/result.png")


if __name__ == '__main__':
    main()