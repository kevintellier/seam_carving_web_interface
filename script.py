from PIL import Image
import sys
import os

def silentremove(filename):
	try:
		os.remove(filename)
	except OSError:
		pass

def main():
	mode = sys.argv[1]
	if mode == "resize":
		filename=sys.argv[2]
		new_x=sys.argv[3]
		new_y=sys.argv[4]
		os.system("scip\\seam-carving.exe static\\uploads\\" + filename +" "+ mode + " " +new_x + " " +new_y)
		filename_1, file_extension = filename.split(".")
		silentremove("static\\processed\\"+filename_1+".png")
		os.rename('resultBoat.png', "static\\processed\\"+filename_1+".png")
		silentremove('resultBoat.png')
	elif mode =="mask":
		filename=sys.argv[2]
		filename2=sys.argv[3]
		os.system("scip\\seam-carving.exe static\\uploads\\" + filename +" "+ mode + " static\\uploads\\" + filename2)
		filename_1, file_extension = filename.split(".")
		silentremove("static\\processed\\"+filename_1+".png")
		os.rename('resultBoat.png', "static\\processed\\"+filename_1+".png")
		silentremove('resultBoat.png')
	elif mode =="accent":
		filename=sys.argv[2]
		filename2=sys.argv[3]
		new_x=sys.argv[4]
		new_y=sys.argv[5]
		os.system("scip\\seam-carving.exe static\\uploads\\" + filename +" "+ mode + " static\\uploads\\" + filename2 + " " +new_x + " " +new_y)
		filename_1, file_extension = filename.split(".")
		silentremove("static\\processed\\"+filename_1+".png")
		os.rename('resultBoat.png', "static\\processed\\"+filename_1+".png")
		silentremove('resultBoat.png')
	return 0

if __name__ == '__main__':
	main()