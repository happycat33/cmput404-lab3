#!/usr/bin/env python3 

# ^ tells script what to execute with
#
# NOTE: All code below was taken from the Winter 2022 pre recorded lab (by Zoe Riell)

import os
import json

print("Content-Type: text/html")
print()
print(f"<p>USER_AGENT={os.environ['HTTP_USER_AGENT']}</p>")
