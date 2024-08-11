#!/usr/bin/env python3

import sys
import utils

windowList = utils.run_command("yabai -m query --windows --space")

for window in windowList:
    utils.run_command(f"yabai -m window {window.get("id")} --toggle zoom-fullscreen")