#!/usr/bin/python3

import argparse
from keyat.interface import Interface

keyat = Interface("/dev/ttyUSB0")

# Args
parser = argparse.ArgumentParser(conflict_handler='resolve')
keyat.add_args(parser)
args = parser.parse_args()
keyat.parse_args(args)

if args.string is not None:
    keyat.send()
