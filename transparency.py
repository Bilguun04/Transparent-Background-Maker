from PIL import Image
import os

def make_background_transparent(image_name):
    # Get the full path of the image file based on the script's current working directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_directory, image_name)

    # Open the image using PIL
    image = Image.open(image_path)

    # Convert the image to RGBA mode
    image = image.convert("RGBA")

    # Load pixel data using the load() method
    pixels = image.load()

    # Get image dimensions
    width, height = image.size

    # Create a new image with RGBA mode and transparent background
    transparent_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    # Load pixel data for the new image
    transparent_pixels = transparent_image.load()

    # Loop through each pixel of the original image
    for x in range(width):
        for y in range(height):
            # Get the RGBA values of the current pixel
            r, g, b, a = pixels[x, y]

            # Set the pixel data in the new image
            transparent_pixels[x, y] = (r, g, b, a)

    # Save the transparent image
    transparent_image.save("transparent_" + image_name, format="PNG")

make_background_transparent(input())