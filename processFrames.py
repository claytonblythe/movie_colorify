from PIL import Image
import glob
from tqdm import tqdm
import os

new_size=(1,1080)
filenames = glob.glob('*.png')
total_width = len(filenames) * new_size[0]
max_height = new_size[1]
x_offset = 0

new_im = Image.new('RGB', (total_width, max_height))
for i in tqdm(range(1, len(filenames))):
  new_size=(1,1080)
 # my_filename = 'time_%s.jpg' % (str(i+1))
  my_file= Image.open('outputFrame_%s.png' % str('%06d' % (i+1)))
  my_val = my_file.quantize(1).convert('RGB').getpixel((0,0))
  total_new_pixels = new_size[0] * new_size[1]
  list_of_rgbs = [my_val] * total_new_pixels
  im2 = Image.new('RGB',new_size)
  im2.putdata(list_of_rgbs)
  new_im.paste(im2,(x_offset,0))
  x_offset += new_size[0]
  im2.close()
  my_file.close()

current_dir = os.path.basename(os.getcwd())
new_im.save(current_dir + '_finished_image.png')


resize_ratio2 = (1920,1080)

new_im2 = new_im.resize(resize_ratio2, Image.ANTIALIAS)
new_im2.save(current_dir + '_finished_image_resized_1920,1080.png')
