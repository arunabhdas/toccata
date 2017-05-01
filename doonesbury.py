#!/usr/bin/python3

import sys, argparse, logging
# Make it work for Python 2+3 and with Unicode
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str
import json
import urllib.request
from pprint import pprint
from PIL import Image, ImageChops


def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)

    print ("Welcome to doonesbury. A python tool for image editing. Doonesbury can center-crop your image")
    logging.info("Usage is ./doonesbury.py --input inputfile.png -x 320 -y 480")
    logging.debug("Input : %s" % args.input)

    width = int(args.xdimension)
    height = int(args.ydimension)
    logging.debug("Width : %s" % width)
    logging.debug("Input : %s" % height)

    f = open(args.input, 'rb')
    img = Image.open(f)
    area = (width/2 - height/2, 0, width/2 + height/2, height)
    cropped_image = img.crop(area)
    cropped_image.save("cropped_" + args.xdimension + "x" + args.ydimension + ".png")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = "./doonesbury.py --input inputfile.png -x 320 -y 480",
        epilog = "Inputfile, width and height should be passed in as params '%(prog)s @inputfile.png'.",
        fromfile_prefix_chars = '@' )

    parser.add_argument(
        "-v",
        "--verbose",
        help="increase output verbosity",
        action="store_true")

    parser.add_argument('-i', '--input',
        default='inputfile.png',
        required=True,
        help='inputfile')

    parser.add_argument('-x', '--xdimension',
        default='320',
        required=True,
        help='width')

    parser.add_argument('-y', '--ydimension',
        default='480',
        required=True,
        help='height')


    args = parser.parse_args()

    if args.verbose:
        loglevel = logging.debug
    else:
        loglevel = logging.INFO

    main(args, loglevel)
