from config import *
import characters

from PIL import Image, ImageDraw

horizontal_offset = unit  # Variable
vertical_offset = unit0_5  # Constant


def find_text_width(text):
    width = 0

    for letter in text:
        character = characters.consonants.get(letter)
        width += character.get("size") + unit

    return int(width) + unit


def render_letters(text, image):
    global horizontal_offset

    for letter in text:
        character = characters.consonants.get(letter)
        lines = character.get("lines")

        for line in lines:
            image.line((line[0] + horizontal_offset, line[1] + vertical_offset,
                        line[2] + horizontal_offset, line[3] + vertical_offset), fill=(0, 0, 0), width=line_width)

        horizontal_offset += character.get("size") + unit


def main():
    text_to_render = input("Enter Conlang Text: ")
    text_width = find_text_width(text_to_render)

    base_image = Image.new(mode="RGB", size=(text_width, unit * 3), color=(255, 255, 255))
    text_image = ImageDraw.Draw(base_image)

    text_image.line((0, 0, 0, unit3), fill=(0, 0, 0), width=line_width)
    text_image.line((0, unit3 / 2, text_width, unit3 / 2), fill=(0, 0, 0), width=line_width)
    text_image.line((text_width, 0, text_width, unit3), fill=(0, 0, 0), width=line_width)

    render_letters(text_to_render, text_image)
    base_image.show()


if __name__ == '__main__':
    main()
