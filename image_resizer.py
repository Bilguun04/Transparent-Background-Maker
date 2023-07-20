from PIL import Image

def resize_image(input_path, output_path, new_width, new_height):
    try:
        with Image.open(input_path) as img:
            resized_img = img.resize((new_width, new_height), Image.NEAREST)
            
            resized_img.save(output_path)
            print(f"Image resized and saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

input_image_path = input()
new_width, new_height = map(int, input().split())
output_image_path = input_image_path

resize_image(input_image_path, output_image_path, new_width, new_height)
