from PIL import Image

def transparent_to_white(image_location):
    '''
    It takes image name, returns nothing and replaces old picture with the new one (with same name).
    This function does tranforms picture from transparent to normal picture.
    (Make transparent background to white color)
    '''
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
    '''
    This function takes image name and returns nothing.
    This function transforms picture with black background to transparent. 
    '''
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
    '''
    It take only image name and returns nothing.
    This function reverses white color in the picture to black.
    And replaces old picture with the new one.
    '''
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
