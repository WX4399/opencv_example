#照片去背
from rembg import remove
from PIL import Image
from matplotlib import pyplot as plt

input_path = 'S.png'
output_path = 'output.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
plt.imshow(output)
