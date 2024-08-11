#!/usr/bin/env python3

import sys
import utils

index = int(sys.argv[1]) - 1

windowList = utils.run_command("yabai -m query --windows --space")

windowList.sort(key=lambda e: e.get("id"))
window = windowList[index]
windowId = window.get("id")

utils.run_command(f"yabai -m window --focus {windowId}")
