#!/usr/bin/env python3
"""
Test script to verify server path handling and diagnose nginx proxy issues.
"""

import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

# Test path resolution
appRootPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(f"appRootPath: {appRootPath}")

# Test various paths
test_paths = [
    '/fonts/bootstrap-icons.woff2',
    '/fonts/bootstrap-icons.woff2?e34853135f9e39acf64315236852cd5a',
    'fonts/bootstrap-icons.woff2',
]

for path in test_paths:
    # Strip query string if present
    clean_path = path.split('?')[0] if '?' in path else path

    # Remove leading slash
    if clean_path.startswith('/'):
        clean_path = clean_path[1:]

    filepath = os.path.join(appRootPath, clean_path)

    # Check if file exists
    exists = os.path.exists(filepath)

    print(f"\nOriginal path: {path}")
    print(f"Clean path: {clean_path}")
    print(f"Full filepath: {filepath}")
    print(f"File exists: {exists}")

    if exists:
        # Get file size
        size = os.path.getsize(filepath)
        print(f"File size: {size} bytes")
