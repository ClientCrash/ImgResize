from PIL import Image
import os
import sys
args = sys.argv
basewidth = int(args[1])
baseheigth = int(args[2])
path=args[3]
print("Resizing all png images in " + path + " to [" +str(basewidth) + "x"+str(baseheigth)+ "] .")
files=[]
#m = input("Mode (r/s) > ")
for r, d, f in os.walk(path):
    for file in f:
        if '.png' in file:
            if '.mcmeta' in file:
                continue;
            files.append(os.path.join(r, file))


for f in files:
    print(f)
    img = Image.open(f)
    img=img.resize((basewidth,baseheigth),Image.ANTIALIAS)
    img.save(f)
    print("saved : " + f)
