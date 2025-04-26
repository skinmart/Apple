import os

# Define the path to the folder
folder_path = r"C:\Users\IKMomin\Desktop\SkinMart\Final Mockup\Apple"

# List of common image file extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

# Get all files in the folder
all_files = os.listdir(folder_path)

# Filter only image files
image_files = [file for file in all_files if os.path.splitext(file)[1].lower() in image_extensions]

# Get the first 106 image file names
first_106_images = image_files[:106]

# Print the list of file names
print("First 106 Image File Names:")
for img in first_106_images:
    print(img)

# Optionally, save the list to a text file
output_file = os.path.join(folder_path, "first_106_images.txt")
with open(output_file, "w") as f:
    for img in first_106_images:
        f.write(img + "\n")

print(f"\nList of first 106 images saved to: {output_file}")