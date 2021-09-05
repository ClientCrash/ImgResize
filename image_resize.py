from PIL import Image
import os
basewidth = int(input("w>"))
path=input("p>")
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
    img=img.resize((8,8),Image.ANTIALIAS)
    img.save(f)
    print("saved : " + f)
