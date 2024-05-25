from helper import *

from PIL import Image, ImageDraw


def main():
    text_to_render = input("Text To Transliterate: ")
    text_width = find_text_width(text_to_render)

    # Generating The Base Blank Image
    base_image = Image.new(mode="RGB", size=(text_width, unit * 3), color=(255, 255, 255))
    text_image = ImageDraw.Draw(base_image)

    # Rendering Delimiter And Horizontal Rule Lines
    text_image.line((0, 0, 0, unit3), fill=(0, 0, 0), width=line_width)
    text_image.line((0, unit3 / 2, text_width, unit3 / 2), fill=(0, 0, 0), width=line_width)
    text_image.line((text_width, 0, text_width, unit3), fill=(0, 0, 0), width=line_width)

    render_text(text_to_render, text_image)
    base_image.show()


if __name__ == "__main__":
    main()
