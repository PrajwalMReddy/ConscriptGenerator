from config import *
import characters

horizontal_offset = unit  # Variable
vertical_offset = unit0_5  # Constant

short_vowels_list = ('a', 'e', 'i', 'o', 'u')
long_vowels_list = ('ā', 'ē', 'ī', 'ō', 'ū')
vowels_list = short_vowels_list + long_vowels_list

conjunct_consonants_list = ('r', 'l', 'j', 'w')
foreign_consonants_list = {
}


def in_pair(text, count):
    if text[count] in vowels_list:
        return False
    elif (text[count] not in vowels_list and count + 1 == len(text)) \
            or ((text[count] not in vowels_list and text[count + 1] not in vowels_list)
                and (text[count + 1] not in conjunct_consonants_list)):
        return False
    else:
        return True


def find_text_width(text):
    count = 0
    width = 0

    while True:
        if not in_pair(text, count):
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
            if text[count + 1] in long_vowels_list or (count + 2 != len(text) and text[count + 2] in long_vowels_list):
                marking = characters.markings.get("long")
                width += marking.get("size") + unit

            # Base Consonants In Pairs
            character = characters.consonants.get(text[count])
            width += character.get("size") + unit

            # Conjunct Consonants (In Pairs)
            if text[count + 1] in conjunct_consonants_list:
                character = characters.conjunct_consonants.get(text[count + 1])
                width += character.get("size")
                count += 1

            count += 2

        if count >= len(text):
            break

    return int(width) + unit


def render_character(character, image):
    lines = character.get("lines")

    for line in lines:
        image.line((line[0] + horizontal_offset, line[1] + vertical_offset,
                    line[2] + horizontal_offset, line[3] + vertical_offset), fill=(0, 0, 0), width=line_width)


def render_text(text, image):
    count = 0
    global horizontal_offset

    while True:
        if not in_pair(text, count):
            if text[count] in short_vowels_list:
                # Rendering The Individual Short Vowel
                character = characters.individual_vowels.get(text[count])
                render_character(character, image)
                horizontal_offset += character.get("size") + unit
                count += 1

            elif text[count] in long_vowels_list:
                # Rendering The Individual Long Vowel
                marking = characters.markings.get("long")
                render_character(marking, image)
                horizontal_offset += marking.get("size") + unit
                character = characters.individual_vowels.get(short_vowels_list[long_vowels_list.index(text[count])])
                render_character(character, image)
                horizontal_offset += character.get("size") + unit
                count += 1

            else:
                # Rendering The Dead Cross And Consonant
                marking = characters.markings.get("dead")
                render_character(marking, image)
                horizontal_offset += marking.get("size") + unit
                character = characters.consonants.get(text[count])
                render_character(character, image)
                horizontal_offset += character.get("size") + unit
                count += 1

        else:
            # Rendering The Long Marking If Needed
            if text[count + 1] in long_vowels_list or (count + 2 != len(text) and text[count + 2] in long_vowels_list):
                marking = characters.markings.get("long")
                render_character(marking, image)
                horizontal_offset += marking.get("size") + unit

            # Rendering The Base Consonant
            character = characters.consonants.get(text[count])
            render_character(character, image)

            # Rendering The Diacritic Then Conjunct Consonant If Any
            if text[count + 1] in conjunct_consonants_list:
                # Rendering The Vowel Diacritic
                diacritic = characters.diacritic_vowels.get(text[count + 2]) \
                    if text[count + 2] in short_vowels_list \
                    else characters.diacritic_vowels.get(short_vowels_list[long_vowels_list.index(text[count + 2])])

                render_character(diacritic, image)
                horizontal_offset += character.get("size")

                # Rendering The Consonant Conjunct
                conjunct = characters.conjunct_consonants.get(text[count + 1])
                render_character(conjunct, image)
                horizontal_offset += conjunct.get("size") + unit
                count += 1

            # Rendering Diacritic Directly
            else:
                # Rendering The Vowel Diacritic
                diacritic = characters.diacritic_vowels.get(text[count + 1]) \
                    if text[count + 1] in short_vowels_list \
                    else characters.diacritic_vowels.get(short_vowels_list[long_vowels_list.index(text[count + 1])])

                render_character(diacritic, image)
                horizontal_offset += character.get("size") + unit

            count += 2

        if count >= len(text):
            break
