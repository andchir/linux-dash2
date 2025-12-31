#!/usr/bin/env python3
"""
Debug version of server to see what's happening
"""

import os
import sys

# Simulate being the server_py3.py file
server_file = os.path.realpath('/tmp/gh-issue-solver-1767178549239/app/server/server_py3.py')
print(f"__file__ (server_py3.py): {server_file}")

appRootPath = os.path.dirname(os.path.dirname(server_file))
print(f"appRootPath: {appRootPath}")

# Test the font request
request_path = '/fonts/bootstrap-icons.woff2?e34853135f9e39acf64315236852cd5a'
print(f"\nIncoming request: {request_path}")

# Process like the server does
path = request_path
if '?' in path:
    path = path.split('?')[0]
    print(f"After removing query string: {path}")

if path == '/':
    path = 'index.html'

if path.startswith('/'):
    path = path[1:]
    print(f"After removing leading slash: {path}")

filepath = os.path.join(appRootPath, path)
print(f"filepath (before realpath): {filepath}")

filepath = os.path.realpath(filepath)
print(f"filepath (after realpath): {filepath}")

# Security check
if not filepath.startswith(appRootPath):
    print("❌ SECURITY CHECK FAILED - Would return 403")
else:
    print("✓ Security check passed")

    # Check if file exists
    if os.path.exists(filepath):
        print(f"✓ File exists!")
        print(f"File size: {os.path.getsize(filepath)} bytes")
    else:
        print(f"❌ File NOT found - Would return 404")
        print(f"Looking for: {filepath}")

        # Check what's actually there
        parent_dir = os.path.dirname(filepath)
        print(f"\nContents of {parent_dir}:")
        if os.path.exists(parent_dir):
            for item in os.listdir(parent_dir):
                print(f"  - {item}")
        else:
            print(f"  (directory doesn't exist)")
