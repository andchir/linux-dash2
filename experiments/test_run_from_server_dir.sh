#!/bin/bash

cd /tmp/gh-issue-solver-1767178549239/app/server

echo "Current directory: $(pwd)"
echo "Running: python3 server_py3.py --port 8091 &"

python3 server_py3.py --port 8091 &
PID=$!

sleep 2

echo -e "\n=== Testing requests ==="
echo "Test 1: GET /"
curl -s -o /dev/null -w "HTTP %{http_code}\n" http://localhost:8091/

echo "Test 2: GET /fonts/bootstrap-icons.woff2"
curl -s -o /dev/null -w "HTTP %{http_code}\n" http://localhost:8091/fonts/bootstrap-icons.woff2

echo "Test 3: GET /fonts/bootstrap-icons.woff2?e34853135f9e39acf64315236852cd5a"
curl -s -o /dev/null -w "HTTP %{http_code}\n" 'http://localhost:8091/fonts/bootstrap-icons.woff2?e34853135f9e39acf64315236852cd5a'

# Kill the server
kill $PID 2>/dev/null
