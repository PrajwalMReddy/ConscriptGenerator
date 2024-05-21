from PIL import Image, ImageDraw

unit = 50
unit2 = unit * 2
unit3 = unit * 3
unit0_5 = unit * 0.5


# TODO
def find_text_width(text):
    return unit * len(text)  # Temporary Code


def main():
    text_to_render = input("Enter Conlang Text: ")
    text_width = find_text_width(text_to_render)

    base_image = Image.new(mode="RGB", size=(text_width, unit * 3), color=(255, 255, 255))
    text_image = ImageDraw.Draw(base_image)

    text_image.line((0, 0, 0, unit3), fill=(0, 0, 0), width=10)
    text_image.line((0, unit3/2, text_width, unit3/2), fill=(0, 0, 0), width=10)
    text_image.line((text_width, 0, text_width, unit3), fill=(0, 0, 0), width=10)

    base_image.show()


if __name__ == '__main__':
    main()
