import os
from PIL import Image

def main(main_images_folder, new_width=800):
  if not os.path.isdir(main_images_folder):
    raise NotADirectoryError(f'{main_images_folder} doesn\'t exist')
  
  for root, directories, files in os.walk(main_images_folder):
    for file in files:
      full_file_path = os.path.join(root, file)
      filename, extension = os.path.splitext(file)
      converted_tag = '_CONVERTED'
      new_file = filename + converted_tag + extension
      new_full_file_path = os.path.join(root, new_file)
      
      if converted_tag in full_file_path:
        continue

      img_pillow = Image.open(full_file_path)

      width, height = img_pillow.size
      new_height = round(new_width * height / width)
      
      new_image = img_pillow.resize((new_width, new_height), Image.LANCZOS)
      new_image.save(
        new_full_file_path,
        optimize=True,
        quality=70
      )

      new_image.close()
      img_pillow.close()

if __name__ == '__main__':
  main_images_folder = 'images'
  main(main_images_folder, new_width=600)
