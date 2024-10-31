from PIL import Image
import os

# Set the path to the image
input_path = r'C:\Projects\eDataPlayground\eDataPlayground\DSC_7238.jpg'  # Ensure this path is correct

# Print the path to verify
print(f'Checking file at: {input_path}')

# Check if the file exists
if not os.path.exists(input_path):
    print(f'File not found: {input_path}')
else:
    # Set the output path to save the resized image in the same directory with a new name
    output_path = r'C:\Projects\eDataPlayground\eDataPlayground\DSC_2024_resized.jpg'

    try:
        # Open the image
        img = Image.open(input_path)

        # Resize and crop to a 600x600 square
        width, height = img.size
        min_dim = min(width, height)

        # Calculate cropping box to get a centered square
        left = (width - min_dim) / 2
        top = (height - min_dim) / 2
        right = (width + min_dim) / 2
        bottom = (height + min_dim) / 2
        img_cropped = img.crop((left, top, right, bottom))

        # Resize to 600x600 pixels
        img_resized = img_cropped.resize((600, 600), Image.BICUBIC)

        # Save the resized image as a JPEG in the specified directory
        img_resized.save(output_path, format="JPEG", quality=85, optimize=True)

        print(f'Resized image saved to: {output_path}')

    except Exception as e:
        print(f'An error occurred: {e}')