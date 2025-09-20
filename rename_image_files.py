import os



def rename_images(directory):
  files = os.listdir(directory)
  
  for idx, f in enumerate(files):
    _, ext = os.path.splitext(f)

    new_name = f'{idx}' + ext

    os.rename(f'./{f}', f'images/{new_name}')



rename_images('./images')


