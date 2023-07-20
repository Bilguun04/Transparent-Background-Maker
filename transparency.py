from PIL import Image

pieces = ['R', 'N', 'B', 'Q', 'K', 'P']

def transparent_to_white(image_location):
    img = Image.open(image_location)
    datas = img.getdata()
    new_data = []
    for data in datas:
        if data == (255, 255, 255, 0):
            new_data.append((255, 255, 255))
        else:
            new_data.append(data)
    new_image = Image.new('RGB', img.size)
    new_image.putdata(new_data)
    new_image.save(image_location)

def black_to_transparent(image_location):
    img = Image.open(image_location)
    img.convert('RGBA')
    datas = img.getdata()
    new_data = []
    for data in datas:
        if data == (0, 0, 0):
            new_data.append((0, 0, 0, 0))
        else:
            new_data.append(data)
    new_image = Image.new('RGBA', img.size)
    new_image.putdata(new_data)
    new_image.save(image_location)

def white_to_black(image_location):
    img = Image.open(image_location)
    datas = img.getdata()
    new_data = []
    for data in datas:
        if data[3] == 0:
            new_data.append(data)
        else:
            new_data.append((0, 0, 0))
    new_image = Image.new('RGBA', img.size)
    new_image.putdata(new_data)
    new_image.save(image_location)