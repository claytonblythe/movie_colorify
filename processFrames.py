#!/home/claytonblythe/anaconda3/bin/python
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
    parser.add_argument('-w', '--width', type=int, default=1920, help='width of wallpaper in pixels')
    parser.add_argument('-v', '--height', type=int, default=1080, help='height of wallpaper in pixels (number of pixels in vertical direction)')
    # Array for all arguments passed to script
    args = parser.parse_args()
    # Assign args to variables
    movie_file = args.movie_file
    width = args.width
    height = args.height
    # Return all variable values
    return movie_file, width, height

 # Match return values from get_arguments()
 # and assign to their respective variables
movie_file, width, height  = get_args()

def make_frames(movie_file):
    os.system('ffmpeg -i {} -vf scale=8:8 im_%06d.png > /dev/null 2>&1'.format(movie_file))

print('Converting movie to frames...please be patient. This may take up to a few minutes')
make_frames(movie_file)

new_size=(1,1)
filenames = glob.glob('im*.png')
total_width = len(filenames) * new_size[0]
max_height = new_size[1]
x_offset = 0

new_im = Image.new('RGB', (total_width, max_height))
print('Converting {} frames to wallpaper'.format(movie_file))
for i in tqdm(range(1, len(filenames))):
  new_size=(1,1)
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
new_im.save('../wallpapers/'+ current_dir + '_base_image.png')

# Create an image based on command line width and height arguments
resize_ratio2 = (width,height)
new_im2 = new_im.resize(resize_ratio2, Image.ANTIALIAS)
new_im2.save('../wallpapers/' + current_dir + '_sized_{}x{}.png'.format(width, height))

my_dict = {'3048':'1080', '3840':'2160', '1334':'750'}
for k, v in my_dict.items():
    tmp_new_img = new_im.resize((int(k), int(v)), Image.ANTIALIAS)
    tmp_new_img.save('../wallpapers/' + current_dir + '_sized_{}x{}.png'.format(k, v))
