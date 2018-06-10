from PIL import Image
import sys

def main():
	filename = sys.argv[1]
	im_rgb = Image.open("static/uploads/"+filename)
	im_bw = im_rgb.convert("L")
	im_bw.save("static/processed/"+filename)
	return 0

if __name__ == '__main__':
	main()