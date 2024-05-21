from PIL import Image

unit = 50


# TODO
def find_text_width(text):
    return unit * len(text)  # Temporary Code


def main():
    text_to_render = input("Enter Conlang Text: ")
    text_width = find_text_width(text_to_render)

    image = Image.new(mode="RGB", size=(text_width, unit * 3), color=(255, 255, 255))
    image.show()


if __name__ == '__main__':
    main()
