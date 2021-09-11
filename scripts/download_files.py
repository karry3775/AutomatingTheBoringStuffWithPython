#!/usr/bin/env python

import requests
import argparse
from colorama import Fore

DEFAULT_URL = "https://automatetheboringstuff.com/files/rj.txt"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default=DEFAULT_URL, type=str)
    parser.add_argument("--verbose", default=False)

    args = parser.parse_args()

    res = requests.get(args.url)

    res.raise_for_status()

    # Sample data
    print("Sample data")
    print(Fore.CYAN + res.text[:250] + Fore.RESET)
    print("Exited cleanly!")


if __name__ == "__main__":
    main()
