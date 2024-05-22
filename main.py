from config import *
import characters

from PIL import Image, ImageDraw

horizontal_offset = unit  # Variable
vertical_offset = unit0_5  # Constant


def find_text_width(text):
    count = 0
    width = 0

    while True:
        if text[count] in ('a', 'e', 'i', 'o', 'u'):
            in_pair = False
        else:
            in_pair = True

        if not in_pair:
            character = characters.individual_vowels.get(text[count])
            width += character.get("size") + unit
            count += 1

        else:
            character = characters.consonants.get(text[count])
            width += character.get("size") + unit
            count += 2

        if count >= len(text):
            break

    return int(width) + unit


def render_letters(text, image):
    count = 0
    global horizontal_offset

    while True:
        if text[count] in ('a', 'e', 'i', 'o', 'u'):
            in_pair = False
        else:
            in_pair = True

        if not in_pair:
            # Rendering The Individual Vowel
            character = characters.individual_vowels.get(text[count])
            lines = character.get("lines")

            for line in lines:
                image.line((line[0] + horizontal_offset, line[1] + vertical_offset,
                            line[2] + horizontal_offset, line[3] + vertical_offset), fill=(0, 0, 0), width=line_width)

            horizontal_offset += character.get("size") + unit
            count += 1

        else:
            # Rendering The Base Consonant
            character = characters.consonants.get(text[count])
            lines = character.get("lines")

            for line in lines:
                image.line((line[0] + horizontal_offset, line[1] + vertical_offset,
                            line[2] + horizontal_offset, line[3] + vertical_offset), fill=(0, 0, 0), width=line_width)

            # Rendering The Vowel Diacritic
            diacritic = characters.diacritic_vowels.get(text[count + 1])
            lines = diacritic.get("lines")

            for line in lines:
                image.line((line[0] + horizontal_offset, line[1] + vertical_offset,
                            line[2] + horizontal_offset, line[3] + vertical_offset), fill=(0, 0, 0), width=line_width)

            horizontal_offset += character.get("size") + unit
            count += 2

        if count >= len(text):
            break


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


if __name__ == "__main__":
    main()
