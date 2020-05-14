import argparse

import examples as ex
from ui import Ui

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', nargs='?', default=None)
parser.add_argument('-d', '--depth', nargs='?', default=None, type=int)
parser.add_argument('-p', '--postcond', nargs='?', default=None)
parser.add_argument('-i', '--inline', choices=['t', 'true', 'f', 'false'])

r = parser.parse_args()
ui = Ui(r)
