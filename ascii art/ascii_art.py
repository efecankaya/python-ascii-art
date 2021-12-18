from PIL import Image

ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

asd = len(ASCII_CHARS)

def create_matrix(pixels):
    pixel_matrix = []
    for i in range(0, len(pixels), width):
        pixel_matrix.append(pixels[i:i+width])
    return pixel_matrix

def average_conversion(pixel):
    return int((pixel[0] + pixel[1] + pixel[2]) / 3)

def lightness_conversion(pixel):
    return int((max(pixel[0], pixel[1], pixel[2]) + min(pixel[0], pixel[1], pixel[2])) / 2)

def luminosity_conversion(pixel):
    return int(0.21*pixel[0] + 0.72*pixel[1] + 0.07*pixel[2])

def convert_to_brightness(pixel_matrix, mode):
    conversion = [] 
    for row in pixel_matrix:
        new_row = []
        for pixel in row:
            if mode == "average":
                new_pixel = average_conversion(pixel)
            elif mode == "lightness":
                new_pixel = lightness_conversion(pixel)
            elif mode == "luminosity":
                new_pixel = luminosity_conversion(pixel)
            else:
                raise Exception("wrong mode")
            new_row.append(new_pixel)
        conversion.append(new_row)
    return conversion
    
def convert_to_ascii(brightness):
    ascii_length = len(ASCII_CHARS)
    brightness_length = 256
    map_index = int(brightness * (ascii_length / brightness_length))
    return ASCII_CHARS[map_index] * 2
    

def brightness_to_ascii(brightness_matrix):
    conversion = [] 
    for row in brightness_matrix:
        new_row = []
        for brightness in row:
            new_pixel = convert_to_ascii(brightness)
            new_row.append(new_pixel)
        conversion.append(new_row)
    return conversion


img = Image.open("nature.jpeg")
""" img = Image.open("pineapple.jpeg") """
height = img.height
width = img.width

pixels = list(img.getdata())
pixel_matrix = create_matrix(pixels)
brightness_matrix = convert_to_brightness(pixel_matrix, "luminosity")
ascii_matrix = brightness_to_ascii(brightness_matrix)

for row in ascii_matrix:
    for ascii in row:
        print(ascii, end="")
    print("")