#!/bin/bash

# Test running server from different directories

echo "=== Test 1: Running from repository root ==="
cd /tmp/gh-issue-solver-1767178549239
python3 -c "
import os
import sys
sys.path.insert(0, 'app/server')
file_path = os.path.realpath('app/server/server_py3.py')
print(f'__file__ would be: {file_path}')
app_root = os.path.dirname(os.path.dirname(file_path))
print(f'appRootPath would be: {app_root}')
font_path = os.path.join(app_root, 'fonts', 'bootstrap-icons.woff2')
print(f'Font path would be: {font_path}')
print(f'Font exists: {os.path.exists(font_path)}')
"

echo -e "\n=== Test 2: Running from app directory ==="
cd /tmp/gh-issue-solver-1767178549239/app
python3 -c "
import os
file_path = os.path.realpath('server/server_py3.py')
print(f'__file__ would be: {file_path}')
app_root = os.path.dirname(os.path.dirname(file_path))
print(f'appRootPath would be: {app_root}')
font_path = os.path.join(app_root, 'fonts', 'bootstrap-icons.woff2')
print(f'Font path would be: {font_path}')
print(f'Font exists: {os.path.exists(font_path)}')
"

echo -e "\n=== Test 3: Running from app/server directory ==="
cd /tmp/gh-issue-solver-1767178549239/app/server
python3 -c "
import os
file_path = os.path.realpath('server_py3.py')
print(f'__file__ would be: {file_path}')
app_root = os.path.dirname(os.path.dirname(file_path))
print(f'appRootPath would be: {app_root}')
font_path = os.path.join(app_root, 'fonts', 'bootstrap-icons.woff2')
print(f'Font path would be: {font_path}')
print(f'Font exists: {os.path.exists(font_path)}')
"
