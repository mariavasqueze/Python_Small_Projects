from PIL import Image, ImageFilter

img = Image.open('./assets/pikachu.jpg')
# .filter for effect , #convert for color change
filtered_img = img.convert('L')


filtered_img.show()  # open file
filtered_img.rotate(90)

# resize
resize = filtered_img.resize((300, 300))
# resize keeping aspect ratio
fix = img.thumbnail((400, 400))

# crop
box = (100, 100, 400, 400)
crop = filtered_img.crop(box)

filtered_img.save("grey.png", 'png')
