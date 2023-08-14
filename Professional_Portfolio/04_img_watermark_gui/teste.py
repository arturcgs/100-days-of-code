from PIL import Image, ImageDraw, ImageFont

image = Image.open("data/raw_imgs/potato.jpg")

logo = image.copy()
size = (500, 100)
logo.thumbnail(size)

watermark = image.copy()

width, height = image.size

watermark.paste(logo, (width - 160, height - 100 - 10))
watermark.show()