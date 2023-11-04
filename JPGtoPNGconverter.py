import sys
import os
from PIL import Image

# Grab first and second argument
JPGfolder = sys.argv[1]
PNGfolder = sys.argv[2]

# Check if new folder exist, if not create folder
if not os.path.isdir(PNGfolder):
    os.mkdir(PNGfolder)
   

# Loop through pokedex, convert and save PNG files
for pic in os.listdir(JPGfolder):
    img = Image.open(f'{JPGfolder}{pic}')
    new_path = os.path.splitext(f"{PNGfolder}{pic}")[0]+".png" # Removes the extension of JPG and adds PNG extension.
    print(new_path)
    img.save(new_path, "PNG")





