from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import colorsys
import math
import os, os.path
import argparse


def band(n, steps):
    """Given a set of numbers and a value between 0.0 and 1.0, rounds
    into a series of bands. IE, steps=4 would be [0.0, 0.25, 0.5, 0.75]"""
    return math.floor(n * steps) / steps


def make_test_textures(count, args):
    sq_size = args.texturesize / args.dim
    out_dir = args.outdir

    for i in range(count):
        h = i/count
        img = Image.new('RGB', (args.texturesize, args.texturesize))
        fnt = ImageFont.truetype('fonts/OpenSans-Regular.ttf', int(sq_size * 0.5))
        draw = ImageDraw.Draw(img)

        text_color = tuple(int(v * 255) for v in colorsys.hsv_to_rgb(h, 0.76, 0.5))
        for row in range(int(args.texturesize/sq_size)):
            for col in range(int(args.texturesize/sq_size)):
                is_alt = col % 2 == row % 2
                if is_alt:
                    rgb = tuple(int(v*255) for v in colorsys.hsv_to_rgb(h, 0.25, 1.0))
                else:
                    rgb = tuple(int(v*255) for v in colorsys.hsv_to_rgb(h, 0.75, 1.0))

                x = col * sq_size
                y = row * sq_size

                draw.rectangle((x, y, x+sq_size, y+sq_size), fill=rgb)

                t = chr(ord('A') + row) + str(col)
                text_sz = fnt.getsize(t)
                cx = x + sq_size / 2
                cy = y + sq_size / 2
                draw.text((cx - text_sz[0] / 2, cy - text_sz[1] / 2 - sq_size/10), t, font=fnt, fill=text_color)

        img.save(os.path.join(out_dir, 'img-' + str(i) + '.png'))


def make_matrix(steps, out_dir):
    img = Image.new('RGB', (256, 256))

    for x in range(img.width):
        for y in range(img.height):
            hx = x / float(img.width)
            hy = y / float(img.height)

            if steps > 1:
                hx = band(hx, steps)
                hy = band(hy, steps)
            h = (hx + hy) * 0.5
            s = 1.0
            rgb = colorsys.hsv_to_rgb(h, s, 1.0)
            r, g, b = (int(v * 255) for v in rgb)
            img.putpixel((x,y), (r, g, b))
    img.save(os.path.join(out_dir, 'matrix.png'))


def make_pal(steps, out_dir):
    img = Image.new('RGB', (256, 32))

    for x in range(img.width):
        for y in range(img.height):
            h = x / float(img.width)
            h *= steps
            h = math.floor(h)
            h /= steps
            s = 1.0
            rgb = colorsys.hsv_to_rgb(h, s, 1.0)
            r, g, b = (int(v * 255) for v in rgb)
            img.putpixel((x,y), (r, g, b))
    img.save(os.path.join(out_dir, 'palette.png'))


def main():
    parser = argparse.ArgumentParser("Generate some test images")
    parser.add_argument('count', type=int, default=1, help="Number of test textures")
    parser.add_argument('--outdir', dest='outdir', type=str, default='out', help="Output folder")
    parser.add_argument('--texturesize', dest='texturesize', type=int, default=512)
    parser.add_argument('--dim', dest='dim', type=int, default=8)

    args = parser.parse_args()
    if not os.path.exists(args.outdir):
        os.mkdir(args.outdir)

    count = args.count
    make_pal(count, args.outdir)
    make_matrix(count, args.outdir)
    make_test_textures(count, args)


if __name__ == '__main__':
    main()
