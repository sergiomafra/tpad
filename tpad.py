#!/usr/bin/env python3
import os
import re
import argparse

parser = argparse.ArgumentParser(description="Disables or enables the touchpad.")
parser.add_argument("-d", "--disable", help="disables the touchpad.", action="store_true")
parser.add_argument("-e", "--enable", help="enables the touchpad.", action="store_true")
args = parser.parse_args()

xinput_ids = re.findall('(id=[0-9]+)', os.popen('xinput list | grep -i touchpad').read())

# Disabling
if args.disable and not args.enable:
	for xid in xinput_ids:
		os.system('xinput --disable ' + xid[3:])

# Enabling
if args.enable and not args.disable:
	for xid in xinput_ids:
		os.system('xinput --enable ' + xid[3:])


