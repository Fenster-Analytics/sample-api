#!/bin/sh

echo "=== $@ ==="

# Start the application server
echo "Starting Application Server"
python3 run-server.py

status=$?
if [ $status -ne 0 ]; then
  echo "Application Server failed: $status"
  exit $status
fi
