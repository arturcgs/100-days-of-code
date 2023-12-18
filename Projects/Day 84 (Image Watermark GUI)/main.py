import tkinter as tk
from PIL import Image, ImageDraw, ImageFont


def add_watermark():
    radio = radio_state.get()
    if radio == 1:
        add_watermark_text()
    else:
        add_watermark_img()


def add_watermark_text():
    # reading image
    image = Image.open(source_img_path_entry.get())

    # creating watermark image
    watermark_image = image.copy()
    draw = ImageDraw.Draw(watermark_image)
    font_type = ImageFont.truetype("JetBrains Mono Bold Nerd Font Complete Mono.ttf", 60)

    # get watermark text
    watermark_text = watermark_entry.get()

    # calculate watermark position
    width, height = image.size
    text_width, text_height = draw.textsize(watermark_text, font_type)
    margin = 10

    x = width - text_width - margin
    y = height - text_height - margin

    # draw watermark
    draw.text((x, y), watermark_text, font=font_type)

    # save image
    watermark_image.save(watermarked_img_path_entry.get())


def add_watermark_img():
    # reading image
    image = Image.open(source_img_path_entry.get())
    logo = Image.open(watermark_entry.get())

    # creating watermark image
    watermark_image = image.copy()

    # resize logo
    size = (500, 100)
    logo.thumbnail(size)

    # add logo to img
    width, height = image.size
    watermark_image.paste(logo, (width - 160, height - 100 - 10))

    # save img
    watermark_image.save(watermarked_img_path_entry.get())


# creating window
window = tk.Tk()
window.title("Add Image Watermark")
window.minsize(width=500, height=300)

# welcome message
welcome_text = tk.Label(text="Welcome. This program adds\nWatermark to images", font=("Arial", 24, "bold"))
welcome_text.grid(row=0, column=0, columnspan=2)

# space for source image path
source_img_path_label = tk.Label(text="Type here the path to your source image:", font=("Arial", 14, "bold"))
source_img_path_label.grid(row=1, column=0)
source_img_path_entry = tk.Entry(width=30)
source_img_path_entry.grid(row=1, column=1)

# space for watermarked image path
watermarked_img_path_label = tk.Label(text="Type here the path to save your image:", font=("Arial", 14, "bold"))
watermarked_img_path_label.grid(row=2, column=0)
watermarked_img_path_entry = tk.Entry(width=30)
watermarked_img_path_entry.grid(row=2, column=1)

# radio button
radio_label = tk.Label(text="Choose how to add the watermark: ", font=("Arial", 14, "bold"))
radio_label.grid(row=3, column=0, rowspan=2)

radio_state = tk.IntVar()
radio_button1 = tk.Radiobutton(text="Add Text as watermark", value=1, variable=radio_state)
radio_button2 = tk.Radiobutton(text="Add Logo as watermark", value=2, variable=radio_state)

radio_button1.grid(row=3, column=1)
radio_button2.grid(row=4, column=1)


# space fot text in the watermark
watermark_label = tk.Label(text="Type here the watermark\n(text or path to logo)", font=("Arial", 14, "bold"))
watermark_label.grid(row=5, column=0)
watermark_entry = tk.Entry(width=30)
watermark_entry.grid(row=5, column=1)

# button
button = tk.Button(text="Generate Watermark", command=add_watermark)
button.grid(row=6, column=0, columnspan=2)

window.mainloop()