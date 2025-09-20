from PIL import Image
import os

def convert_images_to_rgb(input_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith((".jpg", ".jpeg", ".png")):  # Check if file is an image
            # Open the image
            img_path = os.path.join(input_folder, filename)
            with Image.open(img_path) as img:
                # Convert the image to RGB if it's grayscale
                if img.mode != "RGB":  # "L" indicates grayscale mode
                    img = img.convert("RGB")
                    print(f"Converted {filename} to RGB")

                # Save the image in the output folder
                output_path = os.path.join(output_folder, filename)
                img.save(output_path)



# Specify input and output folders
input_folder = "images"
output_folder = "rgb_images"

# Run the conversion
convert_images_to_rgb(input_folder, output_folder)