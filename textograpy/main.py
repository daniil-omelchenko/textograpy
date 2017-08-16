import os

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


RESOURCES_PATH = os.path.join(os.path.dirname(__file__), '/../resources/')


def textify_matrix(m):
    return '\n'.join(u''.join(row) for row in m)


def get_letter(char):
    height = 30
    width = 18
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(RESOURCES_PATH + 'courier_new.ttf', height)
    draw.text((0, 0), char, (255, 255, 255), font=font)
    t = []
    for i in range(height):
        row = []
        for j in range(width):
            c = img.getpixel((j, i))
            if c > (100, 100, 100):
                row.append(u'#')
            elif c > (20, 20, 20):
                row.append(u'+')
            else:
                row.append(u' ')
        t.append(row)
    return textify_matrix(t)


def glue_letters(letters):
    letters_matrix = [letter.split(u'\n') for letter in letters]
    transposed_letters_matrix = [row for row in zip(*letters_matrix)]
    return textify_matrix(transposed_letters_matrix)


def get_text(text):
    return glue_letters(map(get_letter, text))
