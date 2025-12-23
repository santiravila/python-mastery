import sys

from PIL import Image

images = []

# open binary files from the command line and append them to list
for arg in sys.argv[1:]: # exclude filename
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)

