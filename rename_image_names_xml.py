import xml.etree.ElementTree as ET
import os

def rename_images_in_xml(xml_file, rename_func):
    

    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    for idx, image in enumerate(root.findall('.//image')):
        old_name = image.get('name')
        new_name = rename_func(old_name, idx)
        print(f'{old_name} ------ changeed to ----> {new_name}')
        image.set('name', new_name)
        os.rename(f'images/{old_name}', f'images/{new_name}')

    tree.write('updated_' + xml_file)

def rename_func(old_name, idx):
    # Example: Change the name format
    # Split the name and extension
    _, ext = os.path.splitext(old_name)
    # Modify the base name as needed (e.g., append "_new" to it)
    # print(idx)
    new_base_name = f'{idx}'  # Change this as needed

    return new_base_name + ext


# Put your xml file name 
rename_images_in_xml('old_annotations.xml', rename_func=rename_func)
