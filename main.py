from config import *
import characters

from PIL import Image, ImageDraw

horizontal_offset = unit  # Variable
vertical_offset = unit0_5  # Constant

vowels_list = ('a', 'e', 'i', 'o', 'u', 'ā', 'ē', 'ī', 'о̄', 'ū')
short_vowels_list = ('a', 'e', 'i', 'o', 'u')
long_vowels_list = ('ā', 'ē', 'ī', 'о̄', 'ū')


def find_text_width(text):
    count = 0
    width = 0

    while True:
        if text[count] in vowels_list:
            in_pair = False
        elif (text[count] not in vowels_list and count + 1 == len(text)) \
                or (text[count] not in vowels_list and text[count + 1] not in vowels_list):
            in_pair = False
        else:
            in_pair = True

        if not in_pair:
            # Individual Vowels
            if text[count] in short_vowels_list:
                character = characters.individual_vowels.get(text[count])
                width += character.get("size") + unit
                count += 1

            # Long Vowels + Marking
            elif text[count] in long_vowels_list:
                marking = characters.markings.get("long")
                character = characters.individual_vowels.get(short_vowels_list[long_vowels_list.index(text[count])])
                width += marking.get("size") + unit
                width += character.get("size") + unit
                count += 1

            # Dead Consonants + Marking
            else:
                marking = characters.markings.get("dead")
                character = characters.consonants.get(text[count])
                width += marking.get("size") + unit
                width += character.get("size") + unit
                count += 1

        else:
            # Long Vowels In Pairs
            if text[count + 1] in long_vowels_list:
                marking = characters.markings.get("long")
                width += marking.get("size") + unit

            # Base Consonants In Pairs
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
        if text[count] in vowels_list:
            in_pair = False
        elif (text[count] not in vowels_list and count + 1 == len(text)) \
                or (text[count] not in vowels_list and text[count + 1] not in vowels_list):
            in_pair = False
        else:
            in_pair = True

        if not in_pair:
            if text[count] in short_vowels_list:
                # Rendering The Individual Short Vowel
                character = characters.individual_vowels.get(text[count])
                lines = character.get("lines")

                for line in lines:
                    image.line((line[0] + horizontal_offset, line[1] + vertical_offset,
                                line[2] + horizontal_offset, line[3] + vertical_offset), fill=(0, 0, 0), width=line_width)

                horizontal_offset += character.get("size") + unit
                count += 1

            elif text[count] in long_vowels_list:
                # Rendering The Individual Long Vowel
                marking = characters.markings.get("long")
                marking_lines = marking.get("lines")

                character = characters.individual_vowels.get(short_vowels_list[long_vowels_list.index(text[count])])
                lines = character.get("lines")

                for marking_line in marking_lines:
                    image.line((marking_line[0] + horizontal_offset, marking_line[1] + vertical_offset,
                                marking_line[2] + horizontal_offset, marking_line[3] + vertical_offset), fill=(0, 0, 0),
                               width=line_width)

                horizontal_offset += marking.get("size") + unit

                for line in lines:
                    image.line((line[0] + horizontal_offset, line[1] + vertical_offset,
                                line[2] + horizontal_offset, line[3] + vertical_offset), fill=(0, 0, 0), width=line_width)

                horizontal_offset += character.get("size") + unit
                count += 1

            else:
                # Rendering The Dead Cross And Consonant
                marking = characters.markings.get("dead")
                marking_lines = marking.get("lines")

                character = characters.consonants.get(text[count])
                lines = character.get("lines")

                for marking_line in marking_lines:
                    image.line((marking_line[0] + horizontal_offset, marking_line[1] + vertical_offset,
                                marking_line[2] + horizontal_offset, marking_line[3] + vertical_offset), fill=(0, 0, 0),
                               width=line_width)

                horizontal_offset += marking.get("size") + unit

                for line in lines:
                    image.line((line[0] + horizontal_offset, line[1] + vertical_offset,
                                line[2] + horizontal_offset, line[3] + vertical_offset), fill=(0, 0, 0), width=line_width)

                horizontal_offset += character.get("size") + unit
                count += 1

        else:
            # Rendering The Long Marking If Needed
            if text[count + 1] in long_vowels_list:
                marking = characters.markings.get("long")
                marking_lines = marking.get("lines")

                for marking_line in marking_lines:
                    image.line((marking_line[0] + horizontal_offset, marking_line[1] + vertical_offset,
                                marking_line[2] + horizontal_offset, marking_line[3] + vertical_offset), fill=(0, 0, 0),
                               width=line_width)

                horizontal_offset += marking.get("size") + unit

            # Rendering The Base Consonant
            character = characters.consonants.get(text[count])
            lines = character.get("lines")

            for line in lines:
                image.line((line[0] + horizontal_offset, line[1] + vertical_offset,
                            line[2] + horizontal_offset, line[3] + vertical_offset), fill=(0, 0, 0), width=line_width)

            # Rendering The Vowel Diacritic
            diacritic = characters.diacritic_vowels.get(text[count + 1]) \
                if text[count + 1] in short_vowels_list \
                else characters.diacritic_vowels.get(short_vowels_list[long_vowels_list.index(text[count + 1])])
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

    # Generating The Base Blank Image
    base_image = Image.new(mode="RGB", size=(text_width, unit * 3), color=(255, 255, 255))
    text_image = ImageDraw.Draw(base_image)

    # Rendering Delimiter And Horizontal Rule Lines
    text_image.line((0, 0, 0, unit3), fill=(0, 0, 0), width=line_width)
    text_image.line((0, unit3 / 2, text_width, unit3 / 2), fill=(0, 0, 0), width=line_width)
    text_image.line((text_width, 0, text_width, unit3), fill=(0, 0, 0), width=line_width)

    render_letters(text_to_render, text_image)
    base_image.show()


if __name__ == "__main__":
    main()
