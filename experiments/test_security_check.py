#!/usr/bin/env python3
"""
Test the security check logic in server_py3.py
"""

import os

# Simulate the server logic
appRootPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(f"appRootPath: {appRootPath}")
print(f"appRootPath ends with '/': {appRootPath.endswith('/')}")

# Test various paths
test_paths = [
    'fonts/bootstrap-icons.woff2',
    'index.html',
    '../etc/passwd',  # Should be blocked
]

for path in test_paths:
    filepath = os.path.join(appRootPath, path)
    print(f"\n--- Testing: {path} ---")
    print(f"filepath before realpath: {filepath}")

    filepath = os.path.realpath(filepath)
    print(f"filepath after realpath: {filepath}")
    print(f"filepath.startswith(appRootPath): {filepath.startswith(appRootPath)}")

    # Check security
    if not filepath.startswith(appRootPath):
        print("❌ BLOCKED (403 Forbidden)")
    else:
        print("✓ ALLOWED")

        # Check if exists
        if os.path.exists(filepath):
            print(f"✓ File exists")
        else:
            print(f"❌ File not found (404)")
