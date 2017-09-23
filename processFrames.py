from PIL import Image
import glob
from tqdm import tqdm
import os
import argparse

def get_args():
    '''This function parses and return arguments passed in'''
    # Assign description to the help doc
    parser = argparse.ArgumentParser(description='Script to convert movie file to a wallpaper')
    # Add arguments
    parser.add_argument('-f', '--movie_file', type=str, help='movie file name')
    # Array for all arguments passed to script
    args = parser.parse_args()
    # Assign args to variables
    movie_file = args.movie_file
    # Return all variable values
    return movie_file

 # Match return values from get_arguments()
 # and assign to their respective variables
movie_file  = get_args()

def make_frames(movie_file):
    os.system('ffmpeg -i {} -vf scale=8:8 im_%06d.png > /dev/null 2>&1'.format(movie_file))

print('Converting movie to frames...please be patient. This may take up to a few minutes')
make_frames(movie_file)

new_size=(1,1080)
filenames = glob.glob('im*.png')
total_width = len(filenames) * new_size[0]
max_height = new_size[1]
x_offset = 0

new_im = Image.new('RGB', (total_width, max_height))
print('Converting frames to wallpaper')
for i in tqdm(range(1, len(filenames))):
  new_size=(1,1080)
 # my_filename = 'time_%s.jpg' % (str(i+1))
  my_file= Image.open('im_%s.png' % str('%06d' % (i+1)))
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
