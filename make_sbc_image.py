#!/usr/bin/python

import drawsvg as draw
import argparse
import sbcnames
import sbc_constants as sc

global args

def make_sbc_main():
    global args
    args = get_args()

    d = draw.Drawing(500, 500)

    d = sc.draw_chakra(d,args.zodiac)

    # Display
    d.set_pixel_scale(2)
    if args.output_file:
        d.save_svg(args.output_file)
    elif args.zodiac:
        d.save_svg(sc.sbc_image_zodiac)
    else:
        d.save_svg(sc.sbc_image)
    d



def get_args():
    parser = argparse.ArgumentParser(
        prog="make-sbc-image",
        usage="%(prog)s [options]", 
        description=f"make an image of the sarvatobhadra charka, an svg image. default is adityas and \n28 equal nakshatras with krtikka and aryama at the ascending equinox",
    )
    parser.add_argument(
        "-Z",
        "--zodiac",
        action="store_true",
        help="use zodiac signs on the sbc. default is adityas",
    )
    parser.add_argument(
        "-o",
        "--output-file",
        help="name of output file; default is images/sbc.svg, images/sbc-zodiac.svg if -Z is selected",
    )

    args = parser.parse_args()
    return args

make_sbc_main() 
