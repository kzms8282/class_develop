from PIL import Image

def image_output(image, save):
    height = len(image)
    width = len(image[0])
    size = height * width
    img = Image.new("RGB", (width, height))

    array = [] # 2次元配列を1次元に開く
    for i in image:
        array += i
    img.putdata()