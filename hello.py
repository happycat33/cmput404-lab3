#!/usr/bin/env python3

import os
import json

print("Content-Type: text/html")
print()
print(f"<p>USER_AGENT={os.environ['HTTP_USER_AGENT']}</p>")
