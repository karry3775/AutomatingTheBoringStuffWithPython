#!/usr/bin/env python

import webbrowser
import argparse

"""
Program requirements:
- Get a street address from the command line arguments or clipboard
- Opens the webbrowser to the Google maps page for the address
"""

GMAPS_SITE = "https://www.google.com/maps/"


def fmt_addr(addr):
    return addr.replace(" ", "+")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", required=True, help="source location")
    parser.add_argument("--dst", required=True, help="destination location")

    args = parser.parse_args()

    src = fmt_addr(args.src)
    dst = fmt_addr(args.dst)

    print("formatted src: {}".format(src))
    print("formatted dst: {}".format(dst))

    route_addr = "{}dir/{}/{}".format(GMAPS_SITE, src, dst)

    print("Trying to open: {}".format(route_addr))

    # Open webbrowser
    webbrowser.open(route_addr)


if __name__ == "__main__":
    main()


"""
https://www.google.com/maps/dir/385+Massachusetts+Ave,+Arlington,+MA+02474-6720,+USA/425+Medford+St,+Boston,+MA+02129,+USA/
"""
