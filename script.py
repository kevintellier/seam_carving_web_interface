from PIL import Image
import sys
import os

def main():
	filename = sys.argv[1]
	mode = sys.argv[2]
	if mode == "resize":
		os.system("scip\\seam-carving.exe static\\uploads\\" + filename +" "+ mode + " " +sys.argv[3] + " " +sys.argv[4])
	return 0

if __name__ == '__main__':
	main()