# This is a program that I have created to create nice images for possible prints
# or wallpapers of popular movies it usses ffmpg and imagemagik
from PIL import Image
import glob
from tqdm import tqdm
import os

new_size=(1,1080)
filenames = glob.glob('time*')
total_width = len(filenames) * new_size[0]
max_height = new_size[1]
x_offset = 0

new_im = Image.new('RGB', (total_width, max_height))
for i in tqdm(range(1, len(filenames))):
  new_size=(1,1080)
 # my_filename = 'time_%s.jpg' % (str(i+1))
  my_file= Image.open('time_%s.jpg' % (str(i+1)))
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
new_im.save(current_dir + '_finished_image.jpg')


resize_ratio2 = (1920,1080)
resize_ratio3 = (2560,1600)
resize_ratio4 = (1366,768)
resize_ratio5 = (375,667)
resize_ratio6 = (1280,800)
resize_ratio7 = (1440,900)
resize_ratio8 = (1280,1024)
resize_ratio9 = (1680,1050)
resize_ratio10 = (3840,1080)


new_im2 = new_im.resize(resize_ratio2, Image.ANTIALIAS)
new_im2.save(current_dir + '_finished_image_resized_1920,1080.jpg') 
new_im3 = new_im.resize(resize_ratio3, Image.ANTIALIAS)
new_im3.save(current_dir + '_finished_image_resized_2560,1600.jpg')
new_im4 = new_im.resize(resize_ratio4, Image.ANTIALIAS)
new_im4.save(current_dir + '_finished_image_resized_1366,768.jpg')
new_im5 = new_im.resize(resize_ratio5, Image.ANTIALIAS)
new_im5.save(current_dir + '_finished_image_resized_375,667.jpg')
new_im6 = new_im.resize(resize_ratio6, Image.ANTIALIAS)
new_im6.save(current_dir + '_finished_image_resized_1280,1024,1024.jpg')
new_im7 = new_im.resize(resize_ratio7, Image.ANTIALIAS)
new_im7.save(current_dir + '_finished_image_resized_1440,900.jpg')
new_im8 = new_im.resize(resize_ratio8, Image.ANTIALIAS)
new_im8.save(current_dir + '_finished_image_resized_1280,1024.jpg')
new_im9 = new_im.resize(resize_ratio9, Image.ANTIALIAS)
new_im9.save(current_dir + '_finished_image_resized_1680,1050.jpg')
new_im10 = new_im.resize(resize_ratio10, Image.ANTIALIAS)
new_im10.save(current_dir + '_finished_image_resized_3840,1080.jpg')

