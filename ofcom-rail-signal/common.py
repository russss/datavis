from PIL import Image, ImageFont, ImageDraw


def draw_text(img, text, x, y, size=30, face="Regular", color=(230, 230, 230)):
    """ Helper to draw text labels using PIL. """
    # This font path assumes you're using a Mac with Open Sans installed.
    fnt = ImageFont.truetype(f"~/Library/Fonts/OpenSans-{face}.ttf", size)
    d = ImageDraw.Draw(img)
    w, h = d.textsize(text, fnt)
    x -= w // 2
    h -= h // 2
    d.text((x, y), text, font=fnt, fill=color)
    return img


def tile_images(images):
    # Tile the three images side by side
    widths, heights = zip(*(i.size for i in images))
    width = sum(widths)
    height = max(heights)
    output = Image.new("RGB", (width, height))
    x_offset = 0
    for im in images:
        output.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    return output
